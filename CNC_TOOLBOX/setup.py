#!/usr/bin/env python


'''
module to run as admin in order to
install CNC TOOLBOX to the system

sudo code
- check if python is installed on the system

- create desktop shortcut with picture
- add cnc toolbox to path
'''

import sys
import os
import site
import platform
import subprocess
import shutil


def linux_extra_sauce():
    linux_dependencies = [
            'xclip',
            'xsel'
    ]
    for d in linux_dependencies:
        try:  # figure out how to run like in terminal
            p = subprocess.run(["which", str(d)])
            if p.returncode:
                try:
                    p = subprocess.run(['sudo', 'apt-get', 'install', str(d)])
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


def install_packages():
    if site.ENABLE_USER_SITE:
        dst = site.USER_SITE
        cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
        src = os.path.join(cwd,'packages/gscrape.py')
        try:
            shutil.copy(src, dst)
        except Exception as e:
            print(e)


def create_venv():
    pass
    # flesh out plan to create local venv and have
    # the program use it by default


def main():
    if int(sys.version[0]) == 3:  # make sure python3 is being used
        dependencies = [  # define depends
        'setuptools',
        'pyside2==5.13',
        'pyperclip'
        ]
        installed_packages = []
        try:
            packages = subprocess.run([sys.executable, '-m', 'pip', 'list'], stdout=subprocess.PIPE)
            for p in list(packages.stdout.split()):
                s = str(p)[1:].replace("'", "")
                installed_packages.append(s)

            # reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
            # installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
            for d in dependencies:
                if d in installed_packages:
                    print(d, 'dependency is met')
                else:
                    try:  # if not met install it
                        p = subprocess.run([sys.executable,
                                            "-m"
                                            "pip",
                                            "install",
                                            str(d)]
                                           )
                        if p.returncode == 0:
                            pass
                        else:
                            print(str(a), ' may not have installed correctly')
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)
        if platform.system() == 'Linux':
            linux_extra_sauce()

        install_packages()
    else:
        print('please run with python3 not python2')


if __name__ == "__main__":
    main()
    input("Press <enter> to exit")

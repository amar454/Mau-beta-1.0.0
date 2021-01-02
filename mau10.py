#!/usr/bin/python3.8

"""
MAU is a linux imitation made in python
Amar Djulovic & others
2020
"""


class Finder:
    def __init__(self, command):
        self.command = command
        self.commandList = command.split()
        self.keywords = {'echo', 'ls', 'quit', 'exit', 'math', 'help', 'cd',
                         'nset', 'refresh', 'cset', 'open', 'cedit',
                         'cat', 'mkdir', 'mkfile', 'editfile'}

    def mFinder(self):
        # checks for valid keywords, a sort of tokenization system.
        # guides the program to each functions
        # calls command files.
        try:
            if self.commandList[0] in self.keywords:
                pass
        except IndexError:
            return None
        if self.commandList[0] in self.keywords:
            tk = self.commandList[0]
            if tk == 'echo':
                return echo(self.commandList)
            elif tk == 'cset':
                return cset(commandList=self.commandList,
                            rootDir=os.path.dirname
                            (os.path.abspath(__file__)),
                            posixbool=posixorlinux)
            elif tk == 'quit':
                return quitf()
            elif tk == 'exit':
                quit()
            elif tk == 'refresh':
                if posixorlinux:
                    system('clear')
                else:
                    system('cls')
                os.execv(__file__, sys.argv)
            elif tk == 'nset':
                return nsmain(self.commandList, posixorlinux)
            elif tk == 'help':
                return print(helptext)
            elif tk == 'ls':
                return ls(self.commandList, rootDir=os.path.dirname
                (os.path.abspath(__file__)), posixfinder=posixorlinux)
            elif tk == 'cd':
                return cd(commandList=self.commandList,
                          rootDir=os.path.dirname
                          (os.path.abspath(__file__)), helptext=cddoc)
            elif tk == 'cat':
                return cat(self.commandList, os.path.dirname
                (os.path.abspath(__file__)), posixbool=posixorlinux, helpfile=catdoc)
            elif tk == 'mkfile':
                return mkfile(commandList=self.commandList, rootDir=rootDir)
            elif tk == 'mkdir':
                return mkdirMain(commandList=self.commandList, rootDir=rootDir)
            elif tk == 'cedit':
                pass
        else:
            return print(f'{self.commandList[0]}: command not found')


if __name__ == '__main__':

    import sys

    from termcolor import colored
    # from app.ceditbeta.main import *
    from msys.lib.cd import cd
    from msys.lib.cset import cset
    from msys.lib.echo import echo
    from msys.lib.ls import ls
    from msys.lib.nset import nsmain
    from msys.lib.pathdif import replaceHome
    from msys.lib.quit import quitf
    from msys.lib.cat import cat
    from msys.lib.mkdir import mkdirMain
    from msys.lib.mkfile import mkfile
    from os import system
    from msys.lib.posixnt import *
    import base64

    rootDir = os.path.dirname(os.path.abspath(__file__))
    posixorlinux = posixfinder()
    # system('clear') if posixfinder() else system('cls')

    with open(f'{rootDir}/doc/help.txt' if posixorlinux else f'{rootDir}\\doc\\help.txt') as fl:
        helptext = fl.read()
        fl.close()
    with open(r'msys/nml/username.txt' if
              posixorlinux else r'msys\nml\username') as f:
        userName = f.read()
        f.close()
    with open(r'msys/nml/computername.txt' if
              posixorlinux else r'msys\nml\computername') as f:
        computerName = f.read()
        f.close()
    with open(r'msys/nml/consolecolor.txt' if
              posixorlinux else r'msys\nml\consolecolor.txt') as f:
        c_colorsList = f.read().split('\n')
    with open(f'{rootDir}/doc/catdoc.txt' if posixorlinux else f'{rootDir}\\doc\\catdoc.txt')as f:
        catdoc = f.read()
    with open(f'doc/cddoc.txt') as f:
        cddoc = f.read()
    if os.path.exists('msys/nml/psena64'):
        with open('msys/nml/psena64') as f:
            decoded = f.read()
            password = base64.b64decode(decoded).decode("utf-8")

    else:
        with open('msys/nml/psena64', 'w+') as f:
            encoded = input("You don't seem to have a root password. "
                            "Please input one here, and store it somewhere safe because there is"
                            " no recovery if you don't have it\n"
                            "Password: ")

            f.write(base64.b64encode(encoded.encode('utf-8')).decode('utf-8'))

    if posixorlinux:
        system('clear')
    else:
        system('cls')

    while True:
        currPath = os.getcwd()
        permission = 'user'
        userInput = input(
            colored(f'{userName}@{computerName}', c_colorsList[0],
                    attrs=['bold']) + ':' + colored
            (replaceHome(text=currPath, rootDir=os.path.dirname
            (os.path.abspath(__file__))), c_colorsList[1]) + '# ')
        Finder(userInput).mFinder()

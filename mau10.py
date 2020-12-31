#!/usr/bin/python3.8
import sys
import time
from os import system
from termcolor import colored
from msys.lib.cd import *
from msys.lib.cset import cset
from msys.lib.ls import *
from msys.lib.nset import *
from msys.lib.echo import *
from msys.lib.quit import quitf
from msys.lib.refresh import refresh
from app.cedit.main import *

import msys
"""
MAU is a linux imitation made in python
Amar Djulovic & others
2020
"""


def printE(strs):
    return print(strs, end='')


class Finder:
    def __init__(self, command):
        self.command = command
        self.commandList = command.split()
        self.keywords = {'echo', 'ls', 'quit', 'exit', 'math', 'help', 'cd', 'nset', 'refresh', 'cset', 'open', 'cedit'}

    def mFinder(self):
        # checks for valid keywords, a sort of tokenization system.
        # guides the program to each functions
        try:
            if self.commandList[0] in self.keywords:
                pass
        except IndexError:
            return None
        if self.commandList[0] in self.keywords:
            tk = self.commandList[0]
            if tk == 'echo':
                echo(self.commandList)
            elif tk == 'cset':
                return cset(commandList=self.commandList, rootDir=os.path.dirname(os.path.abspath(__file__)))
            elif tk == 'quit':
                return quitf()
            elif tk == 'refresh':
                return refresh()
            elif tk == 'nset':
                return nsmain(self.commandList)
            elif tk == 'help':
                with open(r'doc/help.txt') as f:
                    print(f.read())
                    f.close()
                return None
            elif tk == 'ls':
                return ls(self.commandList, docDir=r'doc')
            elif tk == 'cd':
                return cd(commandList=self.commandList, currpathname=currPath)
            elif tk == 'cedit':
                pass
        else:
            return print(f'{self.commandList[0]}: command not found')


if __name__ == '__main__':


    system('clear')
    with open(r'msys/nml/username') as f:
        userName = f.read()
        f.close()
    with open(r'msys/nml/computername') as f:
        computerName = f.read()
        f.close()
    with open(r'msys/nml/consolecolors') as f:
        c_colorsList = []
        for i in f.readlines():
            c_colorsList.append(i.rstrip('\n'))

    while True:
        currPath = os.getcwd()
        userInput = input(
            colored(f'{userName}@{computerName}', c_colorsList[0].lstrip('console_color1 = '), attrs=['bold']) + ':' + colored
            (f'~' if currPath==os.path.dirname(os.path.abspath(__file__)) else currPath, c_colorsList[1].lstrip('console_color2 = ')) + '% ')
        Finder(userInput).mFinder()

"""
ls function and dependencies in MAU.
Amar Djulovic and others
2020
"""
import math
import os
from datetime import datetime
from pwd import getpwuid


def printE(strs):
    return print(strs, end='')


def t(tm):
    # returns the time last modified formatted nicely
    return datetime.fromtimestamp(os.path.getmtime(f'{tm}')).strftime('%Y-%m-%d %H:%M:%S')


def u(uf):
    # gets the user who made the file
    return getpwuid(os.stat(uf).st_uid).pw_name


def c(cd):
    # checks if the file is a file or a directory
    if os.path.isfile(cd):
        return 'file'
    elif os.path.isdir(cd):
        return 'dir'
    else:
        return 'unknown'


def s(fs):
    # uses algorithm to find the size of a file using the math library and others
    try:
        g = os.path.getsize(fs)
    except OSError:
        return None

    if g == 0:
        return "0B"
    size_name = ("b", "kb", "mb", "gb")
    di = int(math.floor(math.log(g, 1024)))
    p = math.pow(1024, di)
    aas = round(g / p, 2)
    return "%s %s" % (aas, size_name[di])


def confop(timeFiles, userFiles, sizeFiles, typeFiles, hiddenFiles, hiddenFilesA):
    printE('Time last modified: | ' if timeFiles else '')
    printE('User of files: | ' if userFiles else '')
    printE('Size of files: | ' if sizeFiles else '')
    printE('Type: | ' if typeFiles else '')
    printE('Hidden: | ' if hiddenFiles else '')
    print('File names: ')
    for x in os.listdir():
        if hiddenFiles:
            printE(f'{t(x).ljust(20, " ")}| ' if timeFiles else '')
            printE(f"{u(x).ljust(15, ' ')}| " if userFiles else '')
            printE(f"{s(x).ljust(15, ' ')}| " if sizeFiles else '')
            printE(f'{c(x).ljust(5, " ")} | ' if typeFiles else '')
            printE((f'Yes'.ljust(8, " ") + '| ' if x in hiddenFilesA else 'No'.ljust(8, " ") + '| '))
            printE(x)
            print('')
        if not hiddenFiles:
            if x in hiddenFilesA:
                continue
            else:
                printE(f'{t(x).ljust(20, " ")}| ' if timeFiles else '')
                printE(f"{u(x).ljust(15, ' ')}| " if userFiles else '')
                printE(f"{s(x).ljust(15, ' ')}| " if sizeFiles else '')
                printE(f'{c(x).ljust(5, " ")} | ' if typeFiles else '')
                printE(x)
                print('')


def ls(commandList, docDir):
    """
    This is the ls function in Mau. This lists the current directories and subdirectories
    Options are as follows


    -u: returns the user who made the file

    -t: returns the time the file was last modified

    -c: return whether if the file is a dir, file, or other type

    -h: returns the hidden files, like documentation and others

    -s: returns the size of the files in megabytes


    Other things to do:
    Try putting another directory and it will try to list that, otherwise it just skips it and looks for more settings
    """

    HIDDEN_FILES = False
    TIME_FILES = False
    USER_FILES = False
    SIZE_FILES = False
    TYPE_FILES = False
    HELP_REQUEST = False
    ALL_COMMAND = False
    CUST_DIR = False
    hidden = {'.idea', 'help.txt', 'INFO.txt', 'venv', '__pycache__', '__init__'}
    if len(commandList) == 1:
        # default ls configuration
        print('File names: ')
        for i in os.listdir():
            if i not in hidden:
                print(i)
                continue
    else:
        invalidOptions = []
        commandListFinal = []
        validLSOptions = {'-u', '-t', '-h', '-s', '-c', '-a'}
        errorOption = None
        done = False
        # checks for options
        for option in commandList:
            if option in validLSOptions:

                if option == '-u':
                    USER_FILES = True
                    commandListFinal.append(option)

                elif option == '-t':
                    TIME_FILES = True
                    commandListFinal.append(option)
                elif option == '-h':
                    HIDDEN_FILES = True
                    commandListFinal.append(option)
                elif option == '-s':
                    SIZE_FILES = True
                    commandListFinal.append(option)
                elif option == '-c':
                    TYPE_FILES = True
                    commandListFinal.append(option)
                elif option == '-a':
                    HIDDEN_FILES = True
                    TIME_FILES = True
                    USER_FILES = True
                    SIZE_FILES = True
                    TYPE_FILES = True
                    ALL_COMMAND = True
                    commandListFinal.append(option)
            elif option == '--help':
                HELP_REQUEST = True
                commandListFinal.append(option)
                break
            elif option == 'ls':
                commandListFinal.append(option)
                continue

            else:
                errorOption = option
                break
        if errorOption is not None and errorOption[0] == '-':
            pass

        if errorOption is not None and errorOption[0] != '-':
            print(commandList.index(errorOption))
            done = True
        if HELP_REQUEST:
            with open(docDir + '/lsdoc') as f:
                return print(f.read())

        # Time last modified: | User of files: | Size of files: | Type: | Hidden: | File names:

        if not done:
            confop(timeFiles=TIME_FILES, hiddenFiles=HIDDEN_FILES, userFiles=USER_FILES, sizeFiles=SIZE_FILES,
                   typeFiles=TYPE_FILES, hiddenFilesA=hidden)

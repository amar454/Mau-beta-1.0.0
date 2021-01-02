"""
ls function and dependencies in MAU.
Amar Djulovic and others
2020
"""
import math
import os
from datetime import datetime
from pwd import getpwuid


def getSize(start_path='.'):
    total_size = 0
    for dirPath, dirNames, fileNames in os.walk(start_path):
        for f in fileNames:
            fp = os.path.join(dirPath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def replaceHome(text, rootDir):
    text.replace('*', rootDir)


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
        if os.path.isfile(fs):
            g = os.path.getsize(fs)
        elif os.path.isdir(fs):
            g = getSize(fs)
        else:
            g = 0


    except OSError:
        return None
    if g == 0:
        return "0B"
    size_name = ("b", "kb", "mb", "gb")
    di = int(math.floor(math.log(g, 1024)))
    p = math.pow(1024, di)
    aas = round(g / p, 2)
    return "%s %s" % (aas, size_name[di])


def confop(timeFiles, userFiles, sizeFiles, typeFiles,
           hiddenFiles, hiddenFilesA,
           customDir, rootDir, posixfinder):
    printE('Time last modified: | ' if timeFiles else '')
    printE('User of files: | ' if userFiles else '')
    printE('Size of files: | ' if sizeFiles else '')
    printE('Type: | ' if typeFiles else '')
    printE('Hidden: | ' if hiddenFiles else '')
    print('File names: ')
    for x in os.listdir(customDir.replace('*', rootDir) if customDir is not None else None):
        mainSub = customDir.replace('*', rootDir) + ("/" if posixfinder else '\\') if customDir is not None else ''
        if hiddenFiles:
            printE(t(f'{mainSub}{x}').ljust(20, " ") + '| ' if timeFiles else '')
            printE(u(f'{mainSub}{x}').ljust(15, ' ') + '| ' if userFiles else '')
            printE(s(f'{mainSub}{x}').ljust(15, ' ') + '| ' if sizeFiles else '')
            printE(c(f"{mainSub}{x}").ljust(6, " ") + '| ' if typeFiles else '')
            printE((f'Yes'.ljust(8, " ") + '| ' if x in hiddenFilesA else 'No'.ljust(8,
                                                                                     " ") + '| ') if hiddenFiles else '')
            printE(x)
            print('')
        if not hiddenFiles:
            if x in hiddenFilesA or x.startswith('.'):
                continue
            else:
                printE(t(f'{mainSub}{x}').ljust(20, " ") + '| ' if timeFiles else '')
                printE(u(f'{mainSub}{x}').ljust(15, ' ') + '| ' if userFiles else '')
                printE(s(f'{mainSub}{x}').ljust(15, ' ') + '| ' if sizeFiles else '')
                printE(c(f"{mainSub}{x}").ljust(6, " ") + '| ' if typeFiles else '')
                printE(x)
                print('')


def ls(commandList, rootDir, posixfinder):
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

    hidden = {'.idea', 'help.txt', 'INFO.txt', 'venv', '__pycache__', '__init__', '.git'}
    if len(commandList) == 1:
        # default ls configuration
        print('File names: ')
        for i in os.listdir():
            if i not in hidden:
                print(i)
                continue
    else:
        wrongList = []
        commandListFinal = []
        errorOption = None
        done = False
        # checks for options
        for option in commandList:
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
                commandListFinal.append(option)
                break
        if errorOption is not None and errorOption[0] != '-':
            try:
                os.listdir(errorOption.replace('*', rootDir))

                return confop(timeFiles=TIME_FILES, hiddenFiles=HIDDEN_FILES, userFiles=USER_FILES,
                              sizeFiles=SIZE_FILES,
                              typeFiles=TYPE_FILES, hiddenFilesA=hidden,
                              customDir=errorOption, rootDir=rootDir, posixfinder=posixfinder)
            except OSError:
                return print(': '.join(commandListFinal) + ': not a directory or option for ls, '
                                                           'type ls --help for usage')

        if errorOption is not None and errorOption[0] == '-':
            for h in commandList:
                if h == errorOption:
                    wrongList.append(h)
                    return print(f"{': '.join(wrongList)}: unexpected option, type ls --help for usage")
                else:
                    wrongList.append(h)
                    continue
        if HELP_REQUEST:
            with open(f'{rootDir}/doc/lsdoc.txt' if posixfinder else f'{rootDir}\\doc\\lsdoc.txt') as f:
                return print(f.read())

        # Time last modified: | User of files: | Size of files: | Type: | Hidden: | File names:

        if not done:
            confop(timeFiles=TIME_FILES, hiddenFiles=HIDDEN_FILES, userFiles=USER_FILES, sizeFiles=SIZE_FILES,
                   typeFiles=TYPE_FILES, hiddenFilesA=hidden,
                   customDir=None, rootDir=rootDir, posixfinder=posixfinder)
            return None

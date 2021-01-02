import os
from msys.lib import *


def efmain(commandList, rootDir):

    if len(commandList) == 1:
        return print('%s: no input files, type --%s for usage' % (commandList[0], commandList[0]))
    if len(commandList) > 1:

        if os.path.exists(commandList[1].replace('*', rootDir)):
            if os.path.isfile(commandList[1].replace('*', rootDir)):
                if commandList[1].replace('*', rootDir) in systemFiles:
                    return print('editfile: %s: cannot edit system files or files with the same name as system files'
                                 % commandList[1])
                else:
                    with open(commandList[1].replace('*', rootDir), 'r+') as f:
                        print('Welcome to editfile! this is an extremely barebones text editor. '
                              'Type editfile.quit; to end the editing at any line')
                        linesList = []
                        while True:
                            lineInput = input('')
                            if lineInput != 'editfile.quit;':
                                break
                            else:
                                lineInput.append(lineInput)
                                continue
                        f.truncate()
                        f.write('\n'.join(linesList))
                        f.close()

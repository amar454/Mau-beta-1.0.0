import os, sys
def mkdirMain(commandList, rootDir):
    if len(commandList) == 1:
        return None
    if len(commandList)>1:
        if commandList[1] == '--help':
            return None
        try:
            return os.mkdir(f'{str(commandList[1].replace("&", rootDir))}')
        except FileExistsError:
            return print(f'%s: %s: file already exists in directory' % (commandList[0], commandList[1]))


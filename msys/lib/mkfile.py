import os

def mkfile(commandList, rootDir):
    if len(commandList) == 1:
        return None
    elif len(commandList) > 1:
        if os.path.exists(commandList[1]):
            return print(
                '%s: %s: file already exists in directory; try another name' % (commandList[0], commandList[1]))
        open(commandList[1].replace('*', rootDir), 'w+')
        return None

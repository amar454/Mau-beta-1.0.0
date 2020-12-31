"""
cset command and dependencies
Amar Djulovic and others
2020
"""

def cc1(color, rootDir):
    with open(f'{rootDir}/msys/nml/consolecolor.txt', 'r+') as f:
        validColors = {'blue', 'green', 'pink', 'red', 'purple', 'white', 'yellow', ''}
        lines = f.readlines()
        if color in validColors:
            lines[0] = f'{color}'
            f.seek(0)
            f.write('\n'.join(lines))
            f.truncate()
            f.close()
            return None
        else:
            f.close()
            return print(f'cset: cc1: {color}: not a valid color')
def cc2(color, rootDir):
    with open(f'{rootDir}/msys/nml/consolecolor.txt', 'r+') as f:
        validColors = {'blue', 'green', 'pink', 'red', 'purple', 'white', 'yellow', ''}
        lines = f.readlines()

        if color in validColors:
            lines[1] = f'{color}'
            f.seek(0)
            f.write('\n'.join(lines))
            f.truncate()
            f.close()
            return None
        else:
            return print(f'cset: cc2: {color}: not a valid color')
def b():
    pass
def i():
    pass
def cset(commandList, rootDir):
    if len(commandList) > 1:
        if commandList[1] == 'cc1':
            if len(commandList) == 3:
                return cc1(commandList[2], rootDir=rootDir)
        elif commandList[1] == 'cc2':
            if len(commandList) == 3:
                return cc2(commandList[2], rootDir=rootDir)
            else:
                if len(commandList) > 3:
                    return print(f'{commandList[0]}: {commandList[1]}: {commandList[2]}: {commandList[3]}: too many arguments passed')
    else: return None
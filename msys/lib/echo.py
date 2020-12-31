"""
echo function in mau
Amar Djulovic
2020
"""

def echo(commandList):
    commandList.remove('echo')
    return print(*commandList)
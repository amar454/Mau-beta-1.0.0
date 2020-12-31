"""
cd command and dependencies in mau
Amar Djulovic
2020
"""

import os
from itertools import islice

def nth_index(iterable, value, n):
    matches = (idx for idx, val in enumerate(iterable) if val == value)
    return next(islice(matches, n - 1, n), None)

def cd(commandList, currpathname, rootDir):
    commandList.remove('cd')
    CHANGED_DIR = False
    LS_COMMAND = False
    path = None
    try:
        os.chdir(commandList[0])
    except OSError:
        return print(f'cd: {commandList[0]}: not a valid path')
    except IndexError:
        return None
    if len(commandList) > 2:
        for token in commandList:

            if token == '-ls' and not LS_COMMAND:
                LS_COMMAND = True
                continue
            elif token == '-ls' and LS_COMMAND:
                returned = []
                for i in (x for _ in range(commandList.index(nth_index(commandList, '-ls', 2))) for x in commandList):
                    returned.append(i)
            else:
                return print('cd: ')
    else:
        return None
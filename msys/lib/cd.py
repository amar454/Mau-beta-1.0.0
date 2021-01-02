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

def cd(commandList, rootDir, helptext):
    commandList.remove('cd')
    try:
        if commandList[0] == '--help':
            return print(helptext)
        os.chdir(commandList[0].replace('*', rootDir))
    except OSError:
        return print(f'cd: {commandList[0]}: not a valid path')
    except IndexError:
        return None

    else:
        return None
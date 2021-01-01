"""
refresh function in mau
(NON FUNCTIONAL)
Amar Djulovic
2020
"""

import os
import sys
from os import system

def refresh():
    system('clear')
    os.execv(__file__, sys.argv)
import os


def posixfinder():
    if os.name == 'posix':
        return True
    if os.name == 'nt':
        return False
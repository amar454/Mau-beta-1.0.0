#!/usr/bin/python3.8

import time
import os


def progressmain(plist, message, ranged=1, ctstat=1.0, clearstat=False, quitstat=False, quitmessage=None):
    for i in range(ranged):
        if clearstat:
            if os.name == 'posix':
                os.system('clear')
            else:
                os.system('cls')
        for f in plist:
            print(f'{message}{f}', end='\r', flush=True)
            time.sleep(ctstat)
    if quitmessage is not None:
        print(quitmessage)
    print('')
    if quitstat:
        return quit()
    else:
        return None


progressmain(plist=['.', '..', '...'], message='initializing', ranged=3, ctstat=.5, clearstat=True)
quit()

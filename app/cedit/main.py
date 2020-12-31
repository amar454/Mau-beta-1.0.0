#!/usr/bin/python3.8
from os import system

def cedit(text_file):
    uneditableTxt = {'doc/help.txt', 'doc/INFO.txt', 'msys/nml/computername', 'msys/nml/consolecolors', 'msys/nml/username', ''}
    system('clear')
    print('Welcome to Cedit 1.0, usage can be found by exiting and typing \'cedit --help\'. To exit press ctrl+x, '
          'to save press ctrl+s')
    edited = []
    while True:
        line = input('')
        if line == 'cedit.end;':
            break
        edited.append(line)


    with open(text_file, '') as f:
        f.write('\n'.join(edited))


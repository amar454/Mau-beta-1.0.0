Mau-beta-1.0.11

Description:

Mau is an open source, bash-like shell, created in python.
It has similar commands to bash, although they are noticeably different and
encompass different usage and capability.
Mau also includes a bare-bones text editor called editfile, which can be used to 
write basic text files and stuff of the like.
Mau is cross-platform, although mainly designed for Unix-like systems.
Mau is expected to have support until at least 2021


Commands:
    
    echo: ARGS,             returns ARGS as plain text

    quit,                   quits command line

    refresh,                clears the screen

    ls: &[SETTINGS]: &OPT:, lists the current directories files, and subdirectories. If param OPT is filled it will list OPT's files and subdirectories, will return FileNotFoundError if OPT isn't a real directory under the root directory

    cat: FILE,              will print out a FILE's contents

    nset: OPTION: NAME,     will change the name of option if option is a nml system name

    cset: OPTION: NAME,     will change OPTION consoles colored text, with, will throw error is NAME isn't a valid termcolor color.

    cd: DIR                 will change the working directory to DIR if dir is a directory

    mkdir: DIR              will create a directory with DIR's name if the directory does not already exist in the pwd

    mkfile: FILE            will create a file with FILE's name if a name with FILE's name does not already exist in the pwd
    
    editfile: FILE          will open a basic command line text editor to
Tip:
    Type (command) --help for more help with each command

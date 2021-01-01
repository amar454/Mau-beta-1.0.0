

def cat(commandList, rootDir):
    validOptions = {'-l', }
    LINES_COMMANDS = False
    optionList = []
    errorOption = None
    if len(commandList) == 1:
        return print('cat: no input files')
    if len(commandList) == 2:
        try:
            with open(commandList[1].replace('~', rootDir)) as f:
                print(f.read())
                f.close()

        except OSError:
            return print(f'cat: {commandList[1]}: not a valid file or file path')
    for option in commandList:

        if option in validOptions:
            if option == '-l':
                if not LINES_COMMANDS:
                    LINES_COMMANDS = True
                    optionList.append(option)
                else:
                    return print()
        else:
            optionList.append(option)
            errorOption = option
            break
    try:
        with open(errorOption.replace('~', rootDir)) as f:
            print(f.read())
            f.close()

    except OSError:
        return print(f'cat: {commandList[1]}: not a valid file or file path')

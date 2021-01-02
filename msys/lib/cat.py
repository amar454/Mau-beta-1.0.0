def cat(commandList, rootDir, posixbool):
    LINES_COMMANDS = False
    optionList = []
    errorOption = None
    linesCount = 0
    if len(commandList) == 1:
        return print('cat: no input files')
    if len(commandList) == 2:
        if commandList[1] == '--help':
            with open(f'{rootDir}/doc/catdoc' if posixbool else f'{rootDir}\\doc\\catdoc')as f:
                return print(f.read())
        try:
            with open(commandList[1].replace('*', rootDir)) as f:
                print(f.read())
                f.close()
                return None

        except OSError:
            return print(f'cat: {commandList[1]}: not a valid file or file path')
    for option in commandList:
        if option == 'cat':
            continue
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
        with open(errorOption.replace('*', rootDir)) as f:
            print(f.read())
            for _ in f.readlines(): linesCount += 1
            if LINES_COMMANDS:
                print(linesCount)
            print(f.read())
            f.close()
            return None

    except OSError:
        return print(f'cat: {commandList[1]}: not a valid file or file path')

def cat(commandList, rootDir):

        try:
            with open(commandList[1].replace('~', rootDir)) as f:
                print(f.read())
                f.close()

        except OSError:
            return print(f'cat: {commandList[1]}: not a valid file or file path')

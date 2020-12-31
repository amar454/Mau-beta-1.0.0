def pathnaming(rootDir, currentdir):
    if rootDir in currentdir:
        return currentdir.replace(rootDir, '~')
    else:
        return currentdir
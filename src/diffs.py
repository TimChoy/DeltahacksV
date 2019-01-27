def fiveUp(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*5):
        diff[i] = 0
    for i in range(1024*5, len(readRGB)):
        diff[i] =  readRGB[i] - readRGB[i - 5*1024]

    return diff

def fiveDown(readRGB):
    diff = empty(len(readRGB))

    return diff

def fiveRight(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 < 1019):
            diff[i] = readRGB[i] - readRGB[i + 5]
        else:
            diff[i] = 0

    return diff

def fiveLeft(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 > 4):
            diff[i] = readRGB[i] - readRGB[i - 5]
        else:
            diff[i] = 0

    return diff

def tenUp(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*10):
        diff[i] = 0
    for i in range(1024*10, len(readRGB)):
        diff[i] =  readRGB[i] - readRGB[i - 10*1024]

    return diff

def tenDown(readRGB):
    diff = empty(len(readRGB))

    return diff

def tenRight(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 < 1014):
            diff[i] = readRGB[i] - readRGB[i + 10]
        else:
            diff[i] = 0

    return diff

def tenLeft(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 > 9):
            diff[i] = readRGB[i] - readRGB[i - 10]
        else:
            diff[i] = 0

    return diff

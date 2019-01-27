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

    return diff

def fiveLeft(readRGB):
    diff = empty(len(readRGB))

    return diff

def tenUp(readRGB):
    diff = empty(len(readRGB))

    return diff

def tenDown(readRGB):
    diff = empty(len(readRGB))

    return diff

def tenRight(readRGB):
    diff = empty(len(readRGB))

    return diff

def tenLeft(readRGB):
    diff = empty(len(readRGB))

    return diff

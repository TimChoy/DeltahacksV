def fiveUp(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*5):
        diff[i] = 0
    for i in range(1024*5, len(readRGB)):
        diff[i] =  readRGB[i] - readRGB[i - 5*1024]

    return diff

def fiveUpRight(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*5):
        diff[i] = 0
    for i in range(1024*5, len(readRGB)):
            if (i % 1024 < 1019):
                diff[i] =  readRGB[i] - readRGB[i - 5*1024 + 5]
            else:
                diff[i] = 0

    return diff

def fiveUpLeft(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*5):
        diff[i] = 0
    for i in range(1024*5, len(readRGB)):
        if (i % 1024 > 4):
            diff[i] =  readRGB[i] - readRGB[i - 5*1024 - 5]
        else:
            diff[i] = 0

    return diff

def fiveDownRight(readRGB):
    diff = empty(len(readRGB))
        
    for i in range(1024*(1024-5)):
        if (i % 1024 < 1019):
            diff[i] =  readRGB[i] - readRGB[i + 5*1024 + 5]
        else:
            diff[i] = 0
    for i in range(1024*(1024-5), len(readRGB)):
        diff[i] = 0

    return diff

def fiveDownLeft(readRGB):
    diff = empty(len(readRGB))

    for i in range(1024*(1024-5)):
        if (i % 1024 > 4):
            diff[i] =  readRGB[i] - readRGB[i + 5*1024 - 5]
        else:
            diff[i] = 0
            
    for i in range(1024*(1024-5), len(readRGB)):
        diff[i] = 0
            

    return diff

def tenUpRight(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*10):
        diff[i] = 0
    for i in range(1024*10, len(readRGB)):
            if (i % 1024 < 1014):
                diff[i] =  readRGB[i] - readRGB[i - 10*1024 + 10]
            else:
                diff[i] = 0

    return diff

def tenUpLeft(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*10):
        diff[i] = 0
    for i in range(1024*10, len(readRGB)):
        if (i % 1024 > 9):
            diff[i] =  readRGB[i] - readRGB[i - 10*1024 - 10]
        else:
            diff[i] = 0

    return diff

def tenDownRight(readRGB):
    diff = empty(len(readRGB))
        
    for i in range(1024*(1024-10)):
        if (i % 1024 < 1014):
            diff[i] =  readRGB[i] - readRGB[i + 10*1024 + 10]
        else:
            diff[i] = 0
    for i in range(1024*(1024-10), len(readRGB)):
        diff[i] = 0

    return diff

def tenDownLeft(readRGB):
    diff = empty(len(readRGB))

    for i in range(1024*(1024-10)):
        if (i % 1024 > 9):
            diff[i] =  readRGB[i] - readRGB[i + 10*1024 - 10]
        else:
            diff[i] = 0
            
    for i in range(1024*(1024-10), len(readRGB)):
        diff[i] = 0
            

    return diff


def fiveDown(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*(1024-5)):
        diff[i] = readRGB[i] - readRGB[i + 5*1024]
    for i in range(1024*(1024-5), len(readRGB)):
        diff[i] = 0

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
    for i in range(1024*(1024-10)):
        diff[i] = readRGB[i] - readRGB[i + 10*1024]
    for i in range(1024*(1024-10), len(readRGB)):
        diff[i] = 0

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

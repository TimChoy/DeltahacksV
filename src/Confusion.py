# Confusion.py
# Module for dealing with confusion matrix

def calcAccuracy(mat):
    flat = mat[[0, 0, 1, 1], [0, 1, 0, 1]]
    v1, v2, v3, v4 = flat[0], flat[1], flat[2], flat[3]
    wrong = (v3 + v2) / (v1 + v3 + v2 + v4)
    right = (1 - wrong)
    return right
    
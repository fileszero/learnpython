import numpy as np


def Add(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = (x1 * w1) + (x2 * w2)
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def ADD(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

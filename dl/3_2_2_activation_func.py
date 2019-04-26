import numpy as np


def step_function_rustic(x):
    if x > 0:
        return 1
    else:
        return 0


def step_function(x: np.ndarray):
    y = x > 0
    return y.astype(np.int)

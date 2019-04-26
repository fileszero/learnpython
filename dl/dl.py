import numpy as np


def step_function(x: np.ndarray):
    y = x > 0
    return y.astype(np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def identity_function(x):
    return x


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)  ## care over flow
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


def mean_squared_error(y, t):
    """
    4.2.1 2 乗和誤差
    """
    return 0.5 * np.sum((y - t)**2)


def cross_entropy_error(y, t):
    delta = 1e-7  # avoid y=0
    return -np.sum(t * np.log(y + delta))

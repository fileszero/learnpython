import numpy as np

# https://github.com/oreilly-japan/deep-learning-from-scratch

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


def cross_entropy_error(y: np.ndarray, t: np.ndarray):
    """
    Parameters
    ----
    y: ニューラルネットワークの出力
    t: 教師データ
    """
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)

    batch_size = y.shape[0]  # get row count
    delta = 1e-7  # avoid y=0
    return -np.sum(t * np.log(y + delta)) / batch_size


def numerical_diff(f, x):
    diff = 1e-4  # 0.0001
    return (f(x + diff) - f(x - diff)) / (2 * diff)


def tangent_line(f, x):
    d = numerical_diff(f, x)
    # print(d)
    y = f(x) - d * x
    return lambda t: d * t + y


def numerical_gradient(f, x: np.ndarray):
    '''
    偏微分とは、n 変数関数 f(x1, x2, …, xn) のある一つの変数 xi 以外の n-1 個の変数の値を固定することで、f を xi だけの関数とみて、この関数を xi について微分することです。
    すべての変数の偏微分をベクトルとしてまとめたものを勾配（gradient）と言います。
    '''
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)  # type: np.ndarray  # return value/ inilialize by 0

    for idx in range(x.size):
        org_val = x[idx]
        #f(x+h)
        x[idx] = org_val + h
        f1 = f(x)
        #f(x-h)
        x[idx] = org_val - h
        f2 = f(x)
        grad[idx] = (f1 - f2) / (2 * h)

        x[idx] = org_val

    return grad

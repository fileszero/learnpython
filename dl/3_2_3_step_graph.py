import numpy as np
import matplotlib.pylab as plot


def step_function(x: np.ndarray):
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
y2 = sigmoid(x)
plot.plot(x, y)
plot.plot(x, y2)
plot.ylim(-0.1, 1.1)
plot.show()
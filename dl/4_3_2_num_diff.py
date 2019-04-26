import numpy as np
import matplotlib.pylab as plot
import dl


def function_1(x):
    return 0.01 * x**2 + 0.1 * x


x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plot.xlabel("x")
plot.ylabel("y")
plot.plot(x, y)

df1_a = dl.numerical_diff(function_1, 5)
df1_b = function_1(5) - (df1_a * 5)
df1_y = df1_a * x + df1_b
plot.plot(x, df1_y)

df2_y = dl.tangent_line(function_1, 15)(x)
plot.plot(x, df2_y)
plot.show()

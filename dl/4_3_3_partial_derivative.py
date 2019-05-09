import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
'''
偏微分とは、n 変数関数 f(x1, x2, …, xn) のある一つの変数 xi 以外の n-1 個の変数の値を固定することで、f を xi だけの関数とみて、この関数を xi について微分することです。
'''
'''
すべての変数の偏微分をベクトルとしてまとめたものを勾配（gradient）と言います。
'''


def function_2(x: np.ndarray):
    return (x[0]**2) + (x[1]**2)


step = 0.1
x0 = np.arange(-3, 3 + step, step)
x1 = np.arange(-3, 3 + step, step)
print(x0)
print(x1)
X0, X1 = np.meshgrid(x0, x1)
print(X0)
print(X1)

Y = function_2(np.array([X0, X1]))

fig = plt.figure()
ax = Axes3D(fig)

ax.set_xlabel("X0")
ax.set_ylabel("X1")
ax.set_zlabel("f(x)")

ax.plot_wireframe(X0, X1, Y)
# ax.plot_surface(X0, X1, Y)
plt.show()
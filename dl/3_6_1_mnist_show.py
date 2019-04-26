import sys, os
import numpy as np
import mnist
from PIL import Image


def img_show(img):
    pil_image = Image.fromarray(img)
    pil_image.show()


result = mnist.load_mnist(flatten=True, normalize=False)
print(result)
print(type(result))

(x_train, t_train), (x_test, t_test) = mnist.load_mnist(flatten=True, normalize=False)

img = x_train[0]  # type: np.ndarray
label = t_train[0]  # type: np.ndarray

print(img.shape)

img = img.reshape(28, 28)
print(img.shape)
img_show(img)
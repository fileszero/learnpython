import mnist
import numpy as np

(x_train, t_train), (x_test, t_test) = mnist.load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)
print(t_train.shape)

train_size = x_train.shape[0]
batch_size = 10

batch_mask = np.random.choice(train_size, batch_size)

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]

print(x_batch)
print(t_batch)

y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
ya = np.array(y)
print(ya)  #[0.1  0.05 0.6  0.   0.05 0.1  0.   0.1  0.   0.  ]
print(ya.shape)  # (10,)
print(ya.ndim)  # 1
print(ya.size)  #10

yrs = ya.reshape(1, ya.size)
print(yrs)  #[[0.1  0.05 0.6  0.   0.05 0.1  0.   0.1  0.   0.  ]]
print(yrs.shape)  #(1, 10)
print(yrs.ndim)  #2
print(yrs.size)  #10

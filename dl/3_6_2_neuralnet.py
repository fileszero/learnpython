import pickle
import os
import mnist
import numpy as np
import dl

dataset_dir = os.path.dirname(os.path.abspath(__file__))
dataset_dir = os.path.normpath(os.path.join(dataset_dir, "../var"))


def init_network():
    with open(os.path.join(dataset_dir, "sample_weight.pkl"), 'rb') as f:
        network = pickle.load(f)

    return network


def get_data():
    (x_train, t_train), (x_test, t_test) = mnist.load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test


def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = dl.sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = dl.sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = dl.softmax(a3)

    return y


def one_by_one():
    x, t = get_data()
    network = init_network()

    accuracy_count = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y)
        if p == t[i]:
            accuracy_count += 1

    print(accuracy_count / len(t))


def batch():
    x, t = get_data()
    network = init_network()
    batch_size = 100
    accuracy_count = 0
    for i in range(0, len(x), batch_size):
        y = predict(network, x[i:i + batch_size])
        p = np.argmax(y, axis=1)
        accuracy_count += np.sum(p == t[i:i + batch_size])

    print(accuracy_count / len(t))


batch()
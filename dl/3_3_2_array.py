import numpy as np

# (row1,col1) dot (row2,col2)
# must col1 = row2
# result will be (row1,col2)
A = np.array([
    [1, 2],
    [3, 4],
])
B = np.array([
    [5, 6],
    [7, 8],
])
C = np.dot(A, B)

print(str(A.shape) + " dot " + str(B.shape) + " = " + str(C.shape))
print(C)

A = np.array([
    [1, 2],
    [3, 4],
])
B = np.array([
    [5, 6, 7],
    [8, 9, 10],
])
C = np.dot(A, B)

print(str(A.shape) + " dot " + str(B.shape) + " = " + str(C.shape))
print(C)

A = np.array([
    [1, 2, 3],
    [3, 4, 5],
])
B = np.array([
    [5, 6],
    [8, 9],
    [10, 11],
])
C = np.dot(A, B)

print(str(A.shape) + " dot " + str(B.shape) + " = " + str(C.shape))
print(C)

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])
B = np.array([
    [5, 6, 7],
    [8, 9, 10],
])
C = np.dot(A, B)

print(str(A.shape) + " dot " + str(B.shape) + " = " + str(C.shape))
print(C)

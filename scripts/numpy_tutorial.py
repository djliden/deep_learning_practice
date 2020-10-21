# Numpy tutorial from cs231n
# https://cs231n.github.io/python-numpy-tutorial/

# Initialize numpy arrays
import numpy as np

a = np.array([1, 2, 3])
print(type(a)), print(a.shape)

a = np.zeros([2, 2]), a
b = np.ones((1, 2)), b
c = np.full((2, 2), 7)
d = np.eye(2)
e = np.random.random((2, 2))

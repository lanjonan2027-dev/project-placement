import numpy as np

a = np.array([1,2,3])

assert(a.dtype == np.int64)

assert(a.shape == (3,))

print(type(3))
print(type((3)))
print(type((3,)))
print(type(a.shape))

assert(isinstance(a.shape, tuple))
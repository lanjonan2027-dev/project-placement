import numpy as np

a = np.zeros(4)
a == [0, 0, 0, 0]  #compares element-wise..so assert a = [0, 0, 0, 0] gives error

assert np.array_equal(a, [0, 0, 0, 0])

assert (a == np.array([0, 0, 0, 0])).all()

assert(isinstance(a.shape, tuple))

print(a)
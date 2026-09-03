import numpy as np


#One Dimensional Array

a = np.array([0.12, 0.245])

assert(a.shape == (2, ))
assert(a.ndim == 1)


#Two Dimensional Array

a = np.array([[0.12, 0.245],
             [0.9, 0.2],
             ])

assert(a.shape == (2, 2))
assert(a.ndim == 2)

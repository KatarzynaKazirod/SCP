import numpy as np

# EXERCISE 8.1
print('\n\tEXERCISE 8.1\n')
# Create the following NumPy arrays:

# (a) float from 0.0 to 1.0 step 0.1, shape=(11,),
print('\n(a)\n')
a = np.arange(0.0, 1.1, 0.1).reshape(11, )
print(a)
print(a.shape)

# (b) int zeros (1 byte) with shape=(5,6),
print('\n(b)\n')
b = np.zeros(shape=(5,6), dtype = int)
print(b)
print(b.dtype, b.size)

# (c) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2, ..., x**8.
print('\n(c)\n')
c = complex(0,1)**np.arange(9)
print(c)
print(c.shape, c.dtype)
# EXERCISE 8.2
print('\n\tEXERCISE 8.2\n')

# (a) Create an arbitrary one dimensional array called v1.
v1 = np.arange(13, 32)
print(v1)

# (b) Create a new array v2 which consists of the odd indices of v1.
v2 = v1[::2]
print(v2)

# (c) Create a new array v3 in backwards ordering from v1.
v3 = v1[::-1]
print(v3)

# EXERCISE 8.3
print('\n\tEXERCISE 8.3\n')

# (a) Create a two dimensional array called m1, shape=(4,5).
print('\n(a)\n')
m1 = np.arange(20,40).reshape(4,5)
print(m1)
# print(m1.ndim)

# (b) Create a new array m2 from m1, in which the elements of each row are in reverse order.
print('\n(b)\n')
m2 = m1[::, ::-1]
print(m2)
# (c) Create a new array m3 from m1, in which the elements of each column are in reverse order.
print('\n(c)\n')
m3 = m1[::-1]
print(m3)
# (d) Cut of the first and last row and the first and last column of m1.
print('\n(d)\n')
m4 = m1[1:-1, 1:-1]
print(m4)

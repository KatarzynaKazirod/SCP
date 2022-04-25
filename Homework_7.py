from cmath import sqrt
#  EXERCISE 7.1
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'         # return string "Vector(x, y, z)"

    def __eq__(self, other):
        return self is other or\
            self.x == other.x and\
            self.y == other.y and\
            self.z == other.z  # v == w

    def __ne__(self, other):        # v != w
        return not self == other

    def __add__(self, other):    # v + w
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)  # v - w

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z # return the dot product (number)

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x)   # return the cross product (Vector)

    def length(self):
        return sqrt( self.x**2 + self.y**2 + self.z**2)   # the length of the vector

    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended
    def __truediv__(self, skalar):
        return Vector(self.x / skalar, self.y / skalar, self.z / skalar)
        


def  find_axis(v1, v2):
    v3 = v1.cross(v2)
    if v3 == Vector(0, 0, 0):
        raise ValueError('vectors v1 and v2 are parallel (or zero)')
    else: 
        v3Length = v3.length()
        v3Normalized = v3 / v3Length
        return v3Normalized

v1 = Vector(6, 6, 6)
v2 = Vector(-2, -4, 1)   
print(find_axis(v1, v2))

# # EXERCISE 7.2 # Create the following infinite iterators:
import itertools
from re import I

# (a) returning 0, 1, 0, 1, 0, 1, ...,
print('\n\t(a)')
Iter1 = itertools.cycle([0, 1])
print(next(Iter1))
print(next(Iter1))
print(next(Iter1))
print(next(Iter1))
print(next(Iter1))


# (b) returning random sequence with 0 and 1,
print('\n\t(b)')

import random
data = (0,1)
def Random01():
    while(1):
        yield random.choice(data)

RandomGenerator = Random01()
for idx in range(9):
    print(f'sequence {idx + 1}: ', end='')
    for idxn in range(6):
        print(next(RandomGenerator), end='')
    print('')        
    

print()

# (c) returning 0, 1, 0, -1, 0, 1, 0, -1, ..
print('\n\t(c)')
Iter2 = itertools.cycle([0, 1, 0, -1])
print(next(Iter2))
print(next(Iter2))
print(next(Iter2))
print(next(Iter2))
print(next(Iter2))
print(next(Iter2))
print(next(Iter2))
print(next(Iter2))

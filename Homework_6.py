from cmath import sqrt


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
        return Vector(self.y * other.z - self.z * other.y,\
            self.z * other.x - self.x * other.z,\
            self.x * other.y - self.y * other.x)   # return the cross product (Vector)

    def length(self):
        return sqrt( self.x**2 + self.y**2 + self.z**2)   # the length of the vector

    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended

# Exemplary tests.
import math
v = Vector(1, 2, 3)
w = Vector(2, -3, 2)
assert v != w
assert v + w == Vector(3, -1, 5)
assert v - w == Vector(-1, 5, 1)
assert v * w == 2
assert v.cross(w) == Vector(13, 4, -7)
assert v.length() == math.sqrt(14)
S = set([v, v, w])
assert len(S) == 2

print("Exemplary tests passed")


v = Vector(5, 6, 7)
w = Vector(-3, 2, 4)
import math
assert v != w
assert v + w == Vector(2, 8, 11)
assert v - w == Vector(8, 4, 3)
assert v * w == 25
assert v.cross(w) == Vector(10, -41, 28)
assert v.length() == math.sqrt(110)
S = set([v, v, w])
assert len(S) == 2

print('Tests passed')
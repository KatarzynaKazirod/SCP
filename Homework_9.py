import matplotlib.pyplot as plt
import numpy as np

# EXERCISE 9.1 (PLOT)
# Plot functions sin(x), cos(x), and exp(-x) in a range [0,10]. Colors are red, green, and blue, respectively. Lines are solid, dashed, and dotted, respectively. Add a legend.
x = np.arange(0, 10, 0.1)
s = np.sin(x)
c = np.cos(x)
e = np.exp(-x)

plt.plot(x, s, color = 'red', linestyle = 'solid', label = 'sin(x)')
plt.plot(x, c, color = 'green', linestyle = 'dashed', label = 'cos(x)')
plt.plot(x, e, color = 'blue', linestyle = 'dotted', label = 'exp(-x)')
plt.xlabel('x values')
plt.ylabel('sin(x), cos(x) and exp(-x)')
plt.title('fun(x)')
plt.legend()
plt.show()


# EXERCISE 9.2 (SCATTER)
# Generate n=100 random points in a unit square [0,1]x[0,1]. Points are green if the distance from (0,0) is less then 1; they are red otherwise. The marker area of a point (x,y) should be proportional to x+y.

np.random.seed(321)

n = 100
x = np.random.rand(n)
y = np.random.rand(n)

distance00 = np.sqrt(x**2 + y**2)
colors = np.where( (distance00 < 1),'g', 'r')
area = 66*(x + y)

plt.scatter(x, y, s = area, c = colors, alpha = 0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
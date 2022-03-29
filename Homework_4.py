print('EXERCISE 4.1. \np=(x,y)') 
# Let p=(x,y) be a point in a plane. Define the following functions using lambda:

print ('\n\t(a) testing if p is in unit circle\n')

# (x - centerX)² + (y - centerY)² <= r²;  as it is unit circle r = 1 and coordinates of starting point are (0,0)
r = 1 
t_circle = lambda x, y: 'p is in unit circle' if x**2 + y**2 <= r**2 else 'p is not in unit circle'
print(t_circle(2,2))
print(t_circle(1,1))
print(t_circle(1,0))
print(t_circle(-0.2,0.1))
print ('\n\t(b) testing if the coordinates of p are positive\n')

t_positive = lambda x, y: 'The coordinates of p are positive' if (x > 0 and y > 0) else 'the coordinates of p are not positive'
print(t_positive(2,3))
print(t_positive(-2,3))
print(t_positive(-2,-3))
print(t_positive(0,0))


print ('\n\t(c) using a sorting key (y decreasing, x increasing)\n')

p_list = [(2, 6), (-7, 9), (4, 6), (4, 3), (2, 8), (1, 9)] # y decreasing,  x increasing
p_list.sort(key = lambda p: ( -p[1], p[0]))
print(p_list)


print ('\n\t(d) using a sorting key (the sum |x|+|y|)\n')

p_list.sort(key = lambda p: abs(p[0]) + abs(p[1]))  # p[0] is equal to x and p[1] is equal to y
print(p_list)

print ('\nEXERCISE 4.2\n')

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(L)

def reverse_range(L, left, right):

    while left < right:
        n = L[left]
        L[left] = L[right]
        L[right] = n
        left = left + 1
        right = right - 1
    return L

print(f'Reversing a part of a list; iterative version\n{reverse_range(L, 2, 8)}')

#recursive version - no idea at this moment

print ('\nEXERCISE 4.3\n')

print ('\n\t(a) Generating even numbers:\n')

def iter_even():
    i = 0
    while True:
        yield i
        i = i + 2        
for i in iter_even():
    print (i)
    if i > 100:
        break
print('\tor using: next\n ')
x = iter_even()
print(next(x))     
print(next(x)) 

print ('\n\t(b) Generating odd numbers:\n')

def iter_odd():
    i = 1
    while True:
        yield i
        i = i + 2        
for i in iter_even():
    print (i)
    if i > 100:
        break

print('\tor using: next\n ')

x = iter_odd()
print(next(x))     
print(next(x))     

print ('\n\t(c) Generating powers of k:\n')
k = 13
def iter_power(k):
    kp = 0
    while True:
        yield k ** kp
        kp = kp + 1
for i in iter_power(k):
    print (i)
    if i > 10000:
        break

print('\tor using: next\n ')
x = iter_power(k)
print(next(x))   
print(next(x))   
print(next(x))   
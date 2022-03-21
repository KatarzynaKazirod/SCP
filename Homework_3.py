print('\n\nEXERCISE 3.1\n')

cat = 'Kuskus'
for i in range(len(cat)):
    print(f'+---', end='')
print('+')
for i in range(len(cat)):
    print(f'| {cat[i]} ', end='')
print('|')
for i in range(len(cat)):
    print(f'+---', end='')
print('+')


print('\n\nEXERCISE 3.2\n')

from cgitb import text
from unittest import skip

print('\n\tfor loop\n')

for x in range(1,41):
    if x == 13:
        continue
    if x % 5 == 0 and x % 7 == 0:
        print(f'{x} is divided by 5 and 7')
    elif x % 5 == 0:
        print(f'{x} is divided by 5')
    elif x % 7 == 0:
        print(f'{x} is divided by 7')
    elif x % 5 != 0 and x % 7 != 0:
        print(f'{x} is not important')
    else:
        print('error')


print('\n\twhile loop\n')
x = 0
while x < 40:
    x = x + 1
    if x == 13:
        continue
    if x % 5 == 0 and x % 7 == 0:
        print(f'{x} is divided by 5 and 7')
    elif x % 5 == 0:
        print(f'{x} is divided by 5')
    elif x % 7 == 0:
        print(f'{x} is divided by 7')
    elif x % 5 != 0 and x % 7 != 0:
        print(f'{x} is not important')
    else:
        print('check the syntax')
    
print('\n\nEXERCISE 3.3\n')

import math

n = 2022
x = math.pi
x = '{:.{}f}'.format(math.pi, 5)
word = "Python"
polish = "książka"

with open("vars.txt", 'w', encoding = 'utf-8') as file:
    file.write(f'{n}\n')
    file.write(f'{x}\n')
    file.write(f'{word}\n')
    file.write(f'{polish}\n')

with open("vars.txt", "r", encoding="utf-8") as file:
    lines = file.read()
    print(lines)
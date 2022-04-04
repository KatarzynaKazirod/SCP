print('\tEXERCISE 5.1\n')
# For a given directory (top) find the number of bytes taken by PDF files in the directory tree (".pdf" extensions). 
# The code should be in the function find_pdf_size(top). In order to test the current directory we run find_pdf_size(".").

import os
current = os.getcwdb()
print(current)

def find_pdf_size(top):
    pdf_size = 0
    for root, dirs, files in os.walk(top):
        for name in files:
            if name.endswith(".pdf"):
                pdf_size= sum(os.path.getsize(os.path.join(root, name)) for name in files)
    return pdf_size

print('Number of bytes is', find_pdf_size('.'))

print('\n\tEXERCISE 5.2\n')
# Create the function print_working_days(date1, date2), where 'date1' and 'date2' are strings of the form 'YYYY-MM-DD'. 
# The function prints dates of working days (from Monday to Friday) in the given range, 'date2' is excluded.

import datetime

def print_working_days(date1, date2): 
    startDate = datetime.datetime.strptime(date1, '%Y-%m-%d')
    endDate = datetime.datetime.strptime(date2, '%Y-%m-%d')
    while startDate < endDate:
        if startDate.weekday() < 5:
            print(startDate.strftime('%Y-%m-%d'))
        startDate += datetime.timedelta(days=1)

print_working_days("2022-03-28", "2022-04-05")

print('\n\tEXERCISE 5.3\n')
# Create the generator random_walk(start) for a 1D random walker. If a position at a certain moment is x, then the next position can be x+1 or x-1 with equal probabilities. 
# Find the final position after 100 moves (start=0). Repeat experiments.

import random

def random_walk(start):
    x = start
    directions = ['left', 'right']
    for i in range(100):
       step = random.choice(directions)
       if step == 'left': 
           x = x - 1
       elif step == 'right':
           x = x + 1
       else:
           print('WRONG WRONG WRONG')
    return x

print(random_walk(0))
print(random_walk(0))
print(random_walk(0))
print(random_walk(0))


             
from posixpath import split
from wsgiref import headers


print('\n\nEXERCISE 2.1') #Find the number of zeros

long = 4150350**5
print(long)
print('number of zeros = ', str(long).count('0'))

print('\n\nEXERCISE 2.2') 
x = 5
x == 5 and 3                  # 3. x==5 is true, the returned value is the one that has been evaluated last (3)
x == 4 and 3                  # False. First part of the statement is false and the remining part it's not evaluated
3 and x == 5                  # True. x==5 is true and it's printed 
3 and x == 4                  # False. Second part of the statement is false so the result is False 


isinstance(True, int)         # True. True is eaqual to 1 (False to 0); it is true that True is an integer. 
isinstance(True, bool)        # True. print(type(True)) ->  <class 'bool'>

print('\n\nEXERCISE 2.3') 

sum_i = 0
for i in range(1, 2021, 2):
   sum_i = sum_i + i*i
print(sum_i)
    #or second way
print(sum(i * i for i in range(1, 2021, 2)))  

print('\n\nEXERCISE 2.4\n(a)') 

name1 = "Katarzyna"
points = []
for char in name1:
    points.append(ord(char))
print(name1, points)
print('\n(b)') 

from tabulate import tabulate

pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), (3,"Lithium","Li",7), (4,"Beryllium","Be",9), 
    (5,"Boron","B",11), (6,"Carbon","C",12), (7,"Nitrogen","N",14), (8,"Oxygen","O",16), 
    (9,"Fluorine","F",19), (10,"Neon","Ne",20)]

head = ["No.", "Name (en)", "Symbol", "Weight (u)"]

print(tabulate(pt, headers = head, tablefmt = "grind"))

print('\n\nEXERCISE 2.5') 

S = '''Over the last several decades, hydrogen sulfide (H2S) has gained attention
as a new signaling molecule, with extensive physiological and pathophysiological
roles in human disorders affecting vascular biology, immune functions, cellular
survival, metabolism, longevity, development, and stress resistance. Apart from
its known functions in oxidative stress and inflammation, new evidence has emerged
revealing that H2S carries out physiological functions by targeting proteins,
enzymes, and transcription factors through a post-translational modification known
as persulfidation. This review article provides a critical overview of the current
state of the literature addressing the role of H2S in obesity-associated metabolic
disturbances, with particular emphasis on its mechanisms of action in obesity, diabetes,
non-alcoholic fatty liver disease (NAFLD), and cardiovascular diseases.'''



S_sum = sum(len(x) for x in S.split()) # The number of black characters in S
print('The number of black characters in S is equal to', S_sum )
S_words = len(S.split()) # The number of words in S
print('The number of words in S is equal to', S_words)
S_longest = max(S.split(), key = len) # The longest word in S
print('The longest word in S is: ', S_longest)

splitted = S.split(' ')
S_lex = sorted(splitted) # words from S sorted according to the lexicographic order,
print('sorted according to the lexicographic order:\n', S_lex,'\n') 

S_len = sorted(splitted, key = len)
print('sorted according to the length:\n', S_len)

print('\n\nEXERCISE 2.6') 

# Find and explain the results.
t = (2, 4)
#print(t[2])    # 'tuple index out of range'; t[2] means that we want to select the third element, while there are only two in the tuple, therefore no further steps will be performed 
#t.append(6) # tuples are immutable
a, b = t ; print(a, b) # 2 4, previously specified t with two arguments (with values 2 and 4); a,b are arguments with values of 2, 4 

print('\n\nEXERCISE 2.7') 

roman_num = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
arabic_num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

print('\nmethod 1:\n') 

Dict1 = dict(zip(roman_num, arabic_num))
print(Dict1)
print('\nmethod 2:\n')
Dict2 = {}
for i in range(len(roman_num)):
    Dict2[roman_num[i]] = arabic_num[i]

print(Dict2)
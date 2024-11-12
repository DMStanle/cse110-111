n = float(input('Please enter a number: '))
r = round(n)
print(r)


x = 'sun'
y = 'moon'
z = 'stars'

print(x, y, z, sep='-', flush=True)


import math
r = math.sqrt(71)
print(r)



#Functions
#PARAMETER = Piece of data that a function needs to complete it's task.
#ARGUMENT = Value that is passed through a parameter into a function.

age = int(input('How old are you? '))

print(age)

#Optional vs. Name Arguments

lname = input('What is your last name? ')
fname = input("What is your first name? ")
major = input('What is your major? ')

print(fname, lname, major, sep='-')

#MODULES (import MODULE ...etc)

import math

area = float(input('What is the area of the sqaure in square inches? '))

print(f'The size of a side of the square is {math.sqrt(area):.2f} inches. ')
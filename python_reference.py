# *
# !
# ?
# TODO:

#variable, reproducibility
import re
import random
import os
import math
import sys
height = 1.79
weight = 68.7
result = weight/height**2
print(result)

# Boolean
Z = True
print(type(Z))
print('ab'+'cd')

# Python Lists

# Float
height = 1.79
type(height)

# Integers
weight = 67
type(weight)

# Strings
name = 'Marimuthu Ananthavelu'

# Boolean
height = 1.79
tall = True
type(tall)

height_list = [1.59, 1.70, 1.67, 1.80]
print(height_list)
type(height_list)

# collection of values
# may contain duplicates
# contain any and different data types

name_height_list = ['Mari', 1.59, 'Muthu', 1.70, 'Abi', 1.67, 'Rami', 1.80]
print(name_height_list)
type(name_height_list)

# range(): Create a sequence of numbers from 0 to 5, and print each item in the sequence:
    
# Subsetting Lists
name_height_list[2]
name_height_list[0]
name_height_list[-1]
name_height_list[1:3]
name_height_list[1:]
name_height_list[:2]


# List of lists # 2D arrays
Array_2 = [[1, 2], [4, 5]]
len(Array_2)
Array_2[0:1]


# List manipulation
# Adding an element at the end of the list
bigger_list = name_height_list+['next element', "next next element"]
print(bigger_list)

# Adding an element at the beginning of the list
# Adding an element in a specified position within the list
# Removing an element from the end of the list
del(name_height_list[2])
# Removing an element from the beginning of the list
# Removing an element from the specified position within the list

# Replacing al element from the list
name_height_list[2:4] = ["Hello World", 12]
print(name_height_list)


name_height_list[3:5] = ["Life is beautiful", "Congratulations"]
print(name_height_list)


# Dictionaries
names = {'first name': 'Marimuthu', 'last name': 'Ananthavelu'}
print(names)
print(type(names))
print(names['first name'])
# strings to strings
# Strings to numbers
# Numbers to strings
# to anything
new_dictionary = {}
new_dictionary['first item'] = 12
new_dictionary['second item'] = 15
print(new_dictionary)


#Built in functions
x = 5
print(type(x))
y = str(x)
print(type(y))
max([1, 2, 3, 4])
round(1.7, 1)
help(round)
round(1.8, 0)

###########
#Functions#
###########

# Defining a function


def square(value):
    answer = value*value
    return answer


square_of_4 = square(4)
print(square_of_4)
# Range function

#Syntax :range(start, stop, step)
print(range(len([1, 2, 3, 4, 5])))

x = range(3, 6)
for n in x:
    print(n)

# Methods=Functions that belong to objects

max([1, 2, 3.4])
len([1, 2, 3, 4])
# Get index in the list

# Reversing the list

# loops
# while
# for
# recursion

# Sorting

# Searching
# Membership
# Lookin for an element in python

# List comprehension is used to create a list quickly
# List comprehension can aslo modify the list using conditions
# We can replace for loops and nested for loops using list comprehension

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
print(M)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

# Range can be used to quickly define a list of numbers
# * has a purpose here - to unpack items from the object
# range()


# Cube using lambda
def cube(x, y): return print("The product is", x * y)


print(cube(3, 5))

# List comprehension using lambda
a = [(lambda x: x * 2)(x) for x in range(5)]
print(a)

scores = [54, 67, 48, 99, 27]
for i, score in enumerate(scores):
    print(i, score)


def function_name(a, b): return print("The product is: ", a * b)


print(function_name(10, 5))

# map - helps to apply a function quickly using lambda function
# map()
# map(function, something_iterable)


def upper(s):
    return s.upper()


mylist = list(map(upper, ['sentence', 'fragment']))
print(mylist)
# ['SENTENCE', 'FRAGMENT']

# Convert a string representation of
# a number into a list of ints.
list_of_ints = list(map(int, "1234567"))
print(list_of_ints)
# [1, 2, 3, 4, 5, 6, 7]


# enumerate is used to iterate through the index of a list and its actual value
# enumerate()

#Profilers - Memory
# %load_ext memory_profiler
# %mprun -f function_name function_with_arguments

#Profilers - Time
# %load_ext line_profiler
# %lprun -f function_name function_with_arguments

# Get the size of the object
sys.getsizeof(5)


# Retrun 2 values
def get_user(name, birthdate):
    return name, birthdate


name, birthdate = get_user('hello', 'world')

# Variables assignment in python
a = 1
b = 2
a, b = b, a
print(a)
# 2
print(b)
# 1

# Cookie cutter example


class treeModels():
    print("Class for Tree Models classifier")
    a = 10  # Class variable

    def __init__(self, dataset):  # Constructor, Automatically called when the class is called
        self.data = dataset  # Instance variable

    def varTypes(self):  # Methods
        return self.data.dtypes

# Inheritance

# Polymorphism


#dictionaires - merging

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged)
# {'a': 1, 'b': 3, 'c': 4}

# String to title case
mystring = "10 awesome python tricks"
print(mystring.title())
'10 Awesome Python Tricks'

# Get unique elements in the list
mylist = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
print(set(mylist))
# {1, 2, 3, 4, 5, 6}

# And since a string can be treated like a
# list of letters, you can also get the
# unique letters from a string this way:
print(set("aaabbbcccdddeeefff"))
# {'a', 'b', 'c', 'd', 'e', 'f'}
"""
from progress.bar import Bar

bar = Bar('Processing', max=5)
for i in range(5):
    # Do some work
    bar.next()
bar.finish()
"""
# Recursion


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer -In Python, we know that a function can call other functions.
    It is even possible for the function to call itself. These types of construct are termed as recursive functions."""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))


# Collections.counter()

# itertools.combinations()


# Day-1: Data Types
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
ii = 12
dd = 4.0
ss = 'is the best place to learn and practice coding!'
# Read and save an integer, double, and String to your variables.
ii = int(input())
dd = float(input())
ss = str(input())
# Print the sum of both integer variables on a new line.
print(i+ii)
# Print the sum of the double variables on a new line.
print(d+dd)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+ss)


# Day-2: Operators
#!/bin/python3


# Complete the solve function below.

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost*float(tip_percent)/100
    tax = meal_cost*float(tax_percent)/100
    cost = meal_cost+tip+tax
    print(round(cost))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

# *Modularity*

# Packages

# Classes


# Methods

#list is a collections

# Create lists manually
list1234=[1,2,3,4]
print(list1234)

# Create lists using Dictionary


# Create lists using Tuple


# Create lists using Stack


# Create lists using Queue

# Array
# Arrays is a list with indexing
list=[1,2,3]
list[0]

# %%
len(list)

# %%
list_pointer=list

# %%
empty_list=[]

# %%
list2=['hello world','how are you doing']

# %%
list+list2

# %%
items=[0,1,2,3,5]

# %%
sum=0
for item in items:
    sum+=item
    print (sum)

# %%
if 0 in items:
    print ("Hey")

# %%
string="Hello"

# %%
for character in string:
    print (character)

# %%
range(10)

# %%
range_numbers=range(10)

# %%
print (range_numbers)

# %%
for item in range_numbers:
    print (item)

# %%
list1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]

# %%
i=0
while i<=len(list1):
    print (list1[i])
    i=i+3

# %%
"""
### List methods
"""

# %%
list1.append(3)

# %%
print(list1)
#adds teh element at the end of the list

# %%
list1.insert(1,100)

# %%
print (list1)

# %%
list2=[100,200,300]

# %%
list1.extend(list2)

# %%
list1

# %%
list1+list2

# %%
#Sort

# %%
list1.sort()

# %%
list1

# %%
#Find the index of an element in the list

# %%
list1.index(200)

# %%
list1.remove(100)

# %%
list1

# %%
list1.insert(4,400)

# %%
list1

# %%
list1.remove(400)

# %%
list1

# %%
list1.reverse()

# %%
list1

# %%
list1.pop()

# %%
list1.pop(4)

# %%
empty_list=[]

# %%
empty_list.append(4)

# %%
empty_list

# %%
list1

# %%
list1[2:]

# %%
list1[2:3]

# %%
len(list1)

# %%
"""
# 2D array
"""

# %%
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    result=[sum(arr[i-1][j-1:j+2] + [arr[i][j]] + arr[i+1][j-1:j+2]) for j in range(1, 5) for i in range(1, 5)]
    print (result)
    return max(result)

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print((str(result) + '\n'))

# %%
arr[0][0:3]

# %%
arr[1][1]

# %%
arr[2][0:3]

# %%
len(arr)

# %%
len(arr[0])

# %%
range(5)

# %%
lst=[]
for i in range(len(arr)-1):
    for j in range(len(arr[0])-1):
        res=[sum(arr[i][j:j+3]+arr[i+1][j+1]+arr[i+2][j:j+3])]
        print(res)
        lst.append(res)
    return max(lst)

# %%
a = [1,2,3,4]
b = [x*x for x in a]

# %%
a

# %%
b

# %%
for item in b:
    print (item)

# %%
sum([1,2]+[2,3])

# %%

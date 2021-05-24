#Problem definition
# Given: Array of Integers
# Given: Sum
# Given: Find two integers from the array which equals Sum when added.

# Solution design
# 1 to 1 checks using two FOR loops
def twonumberSum2(array,sum):#Define a function
    for item in range(len(array)-1):# For each element in the Array upto the element just before the last element
        firstnumber=array[item]#Store that element
        
        for item2 in range(item+1,len(array)):# Check other elements if they help to get the required sum
            secondnumber=array[item2]
            if firstnumber+secondnumber==sum:
                return [firstnumber, secondnumber]
        return False

array=[1,2,3,4,5]
print(twonumberSum2(array,3))

# Worst Time complexity: 
# Space complxity


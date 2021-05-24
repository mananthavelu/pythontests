#Problem definition
# Given: Array of Integers
# Given: Sum
# Given: Find two integers from the array which equals Sum when added.


def sumproblem(array,sum):
    result=[]
    for number in array:
        potential=sum-number
        if potential in array:
            return[potential,number]
        else:
                result.append(number)
    return []

array=[1,2,3,4,5]
print(sumproblem(array,4))
        
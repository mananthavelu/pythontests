
#Problem definition
# Given: Array of Integers
# Given: Sum
# Given: Find two integers from the array which equals Sum when added.



def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

print(twoNumberSum([1,2,3,4,5],8))

# O(nlog(n)) | O(1) space

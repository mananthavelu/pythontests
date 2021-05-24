# # O(n^2) time | O(n) space


def solution(array,sum):
    array.sort()
    triplets=[]
    for item in range(len(array)-2):
        left=item+1
        right=len(array)-1
        while left<right:
            current_sum=array[item]+array[left]+array[right]
            if current_sum==sum:
                triplets.append([array[item],array[left],array[right]])
                left+=1
                right-=1
            elif current_sum<sum:
                left+=1
            elif current_sum>sum:
                right-=1
    return triplets

print(solution([1,2,3,4,5,6,8,9,10],6))
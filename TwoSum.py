#Example Input: 
nums = [2,7,11,15]
target = 9

#Example Output:
#[0,1]

"""
Given an array of integers (nums) and an integer (target), 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.

:type nums: List[int]
:type target: int
:rtype: List[int]     
"""
def twoSum(nums,target):
    visited = {}
    for i,num in enumerate(nums):
        complement = (target - num)
        if complement in visited:
            return [visited[complement],i]
        else:
            visited[num] = i
    print("end")
        


def bruteForceTwoSum(nums, target):
    #For every number in the list
    for i in range(len(nums)):
        #For every number in the list after i
        for j in range(i+1,len(nums)):
            #If adding the two numbers corresponding to the indices equals the target number...
            if (nums[i]+nums[j]) == target:
                #Print a list with the index of the two numbers that equal 
                print([i,j])
            #Else, continue iterating through the list
            else:
                continue
    #Print "end" once the function has iterated through all numbers in the list
    print("end")

twoSum(nums,target)
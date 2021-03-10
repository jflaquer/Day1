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

#Time complexity: O(n)
def twoSum(nums,target):
    #Creating a dictionary to store all of the numbers as they're visited
    visited = {}
    #For every number in the list, enumerate them to keep track of their index
    for i,num in enumerate(nums):
        #In order to find the number that goes with this one, I calculate the complement and search for that number in my dictionary.
        complement = (target - num)
        #If the complement is in my dicttionary...
        if complement in visited:
            #Return the indices of the current number and the complement, in a list.
            return [visited[complement],i]
        #Otherwise...
        else:
            #Add this number to the dictionary and store it's index as the value. [num:index]
            visited[num] = i
    #Print "end" once it's complete
    print("end")
        

#Time complexity: O(n^2)
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
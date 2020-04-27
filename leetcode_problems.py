"""Leetcode Problem:Given an array of integers,
 return indices of the two numbers such that they add up to a specific target.

Restated: I'm going to return the inidicies of the two numbers in my array that equal a 
specific target number

Clarifying Questions: Could this possibly be a really large list of numbers? 
Are the numbers sorted?

State Assumptions: I am assuming there is only one solution, 
and there will be no repeating elements. 

Explain Rationale: I understand there are much more efficient ways of doing this, 
as looping through all items will always be time inefficient but this is the most
accessible method of solving for me at this point
"""
def two_sum(nums,target):
    
    for i in range(len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return i,j
        

print(two_sum([0,1,2,3],2))


"""
1. Two Sum
Solved
Easy

Topics

Companies

Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution:
    """
    Variant 1: 
    The first approach I tried which I thought was sophisticated but really took me WAY too long
    to implement for really no gain. It tries to exploit the fact that if the difference of the 
    target and a number in the list is greater than the max of the list or is less than the min
    of the list, it cannot be one of the numbers of interest. This solution beats only 5% of 
    accepted solutions in terms of run time. It has run time complexity of O(n^2) while having
    a space complexity of O(n).
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = nums

        # the following while True loop is what I call the max/min filter step which probably 
        # only makes this a less efficient algorithm. 
        while True:
            len_prior = len(nums_copy)
            nums_copy = [num for num in nums_copy if min(nums_copy) <= target - num <= max(nums_copy)]
            if len(nums_copy) == len_prior:
                break
        
        for i in range(len(nums_copy)):
            if (target - nums_copy[i]) in nums_copy[i+1:]:
                elements = [nums_copy[i], target - nums_copy[i]]
                break
    
        if elements[0] != elements[1]:
            element_indices = [nums.index(element) for element in elements]
        else:
            index0 = nums.index(elements[0])
            nums[index0] = elements[0] + 1
            index1 = nums.index(elements[1])
            element_indices = [index0, index1]
        return element_indices


class Solution:
    """
    Variant 2: 
    This literally is the same implementation as Variant 1 except it does not use the min/max 
    filter step, or a nums_copy list. This solution is substantially more efficient than variant 
    1, beating about 39% of other accepted solutions in terms of run time. It has run time 
    complexity of O(n^2) (since we are still doing a search within a for loop), while having a 
    space complexity of O(1). However, the implementation of this particular approach is still not
    as efficient as it could be, and I will propose a better implementation of this same approach 
    for Variant 3.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i+1:]:
                elements = [nums[i], target - nums[i]]
                break
    
        if elements[0] != elements[1]:
            element_indices = [nums.index(element) for element in elements]
        else:
            index0 = nums.index(elements[0])
            nums[index0] = elements[0] + 1
            index1 = nums.index(elements[1])
            element_indices = [index0, index1]
        return element_indices


 class Solution:
    """
    Variant 3:
    Do almost the same thing as Variant 2 except with fewer lines of code. It may not be any 
    different from Variant 2 in terms of exact run time or space complexity.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            rest_of_nums = nums[i+1:]
            if (target - nums[i]) in rest_of_nums:
                indices = [i, rest_of_nums.index(target - nums[i]) + i + 1]
                return indices
    

class Solution:
    """
    Variant 4:
    This is the official solution for Approach 1: 'Brute Force' provided by leetcode. It is a
    slightly different implementation of the same strategy used by Variant 3. It explicitly
    uses a nested for loop to find the pair of numbers that sum to the target instead of using
    the 'in' operator inside only 1 for loop. Like variants 2 and 3 it has a time complexity of
    O(n^2) and a space complexity of O(1).
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


class Solution:
    """
    Variant 5:
    This is the official solution for Approach 2: 'Two-pass Hash Table' provided by leetcode.
    It uses a hash table to reduce the lookup time from O(n) to O(1), trading space for speed.
    A hash table is well-suited for this purpose because it supports fast lookup in near
    constant time (the word "near" is used because if a collision occurred, a lookup could 
    degenerate to O(n) time, but lookup in a hash table should be ammortized O(1) time if the
    hash function is chosen carefully). Thus, the run time complexity for this solution becomes
    O(n), and the space complexity becomes O(n) since extra space is required for the hash table
    to store n elements.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]



class Solution:
    """
    Variant 6:
    This is the official solution for Approach 3: 'One-pass Hash Table' provided by leetcode.
    In 1 for loop, you can do lookup to see if the current element's complement already
    exists in the hash table and if it does, return the pair of indices, before inserting the
    element into the hash table if that block is not hit. So this is more efficient than Variant
    5, but still has linear (O(n)) run time complexity and linear space complexity.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i






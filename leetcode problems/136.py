"""
136. Single Number
Solved
Easy

Topics

Companies

Hint
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

class Solution:
    """
    Variant 1:
    My first successful submission to solve this problem. I would guess that this solution
    does not have a linear time complexity even though the submission was successful since
    the algorithm has to search for a given value being in nums for each iteration of the
    while loop. I am certain however that this solution does have constant space complexity.
    According to LC's analysis tool this solution has time complexity of O(N^2) and space
    complexity of O(1). This solution beats only ~10% of accepted answers in terms of RT
    efficiency but ~95% of accepted answers in terms of memory efficiency. Let's look at
    more optimal approaches.
    """
    def singleNumber(self, nums: List[int]) -> int:
        while nums:
            num = nums.pop()
            if num in nums:
                nums.pop(nums.index(num))
                continue
            else:
                return num



class Solution(object):
    """
    Variant 2:
    The official solution given in the Editorial section for 'Approach 1: List Operation'.
    Note that this solution does not solve the problem with constant space or linear time 
    complexities, as explained in the Complexity Analysis section, which gives O(n^2) and 
    O(n) for the time and space complexity respectively. Also note that LC's analysis tool
    will think that this code has O(n) time complexity, in disagreement with the Editorial. 
    This solution beats ~11% and ~50% of accepted answers in terms of RT and memory 
    efficiency. Given these figures, I don't believe this to be a better approach than 
    Variant 1.
    """
    def singleNumber(self, nums: List[int]) -> int:
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()



from collections import defaultdict
class Solution:
    """
    Variant 3:
    The official solution given in the Editorial section for 'Approach 2: Hash Table'.
    This method offers an improvement from the previous 2 methods in that it solves the
    problem in linear time, though it requires linear memory. Here is the complexity
    analysis provided for this solution:

    ----------------------------------------------------------------------------------

    Complexity Analysis

    Time complexity : O(n⋅1)=O(n). Time complexity of for loop is O(n). Time complexity of hash table(dictionary in python) operation pop is O(1).

    Space complexity : O(n). The space required by hash_table is equal to the number of elements in nums.

    ----------------------------------------------------------------------------------

    This solution beats ~35% and ~25% of accepted answers in run time and memory efficiency
    respectively.
    """
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i

    
    
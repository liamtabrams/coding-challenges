"""
2913. Subarrays Distinct Element Sum of Squares I
Solved
Easy
Topics
Companies
Hint
You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
Example 2:

Input: nums = [1,1]
Output: 3
Explanation: Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

class Solution:
    """
    Variant 1:
    My first successful submission to solve this problem. My hypotheses are that the time
    and space complexities are O(n^2) and O(1) respectively. According to LC's analysis
    tool, my hypothesis about the time complexity was correct but the one about the space
    complexity was incorrect. According to the analysis tool, the space complexity is
    actually O(n), which I am guessing comes from needing to store the subarray variable
    which can be as large as nums itself. Judging from the fact that this submission only
    beats ~6% and ~11% of accepted answers in terms of RT and memory efficiency respectively,
    I think it's safe to say that there are better approaches to solving this problem.
    """
    def sumCounts(self, nums: List[int]) -> int:
        i = 0
        tot_sum_squares = 0
        while i < len(nums):
            for j in range(i+1, len(nums) + 1):
                print(i)
                print(j)
                subarray = nums[i:j]
                num_distinct = len(set(subarray))
                tot_sum_squares += num_distinct**2
            i += 1

        return tot_sum_squares


class Solution:
    """
    Variant 2:
    Arpit Patel's solution from the Solutions section. Though LC's analysis tool claims
    that the RT and space complexity of this solution are O(n^3) and O(n) respectively, 
    this solution outperforms Variant 1 in measurable efficiency, beating ~50% and ~25%
    of accepted answers in terms of RT and memory efficiency respectively.
    """
    def sumCounts(self, nums: List[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                ans.append(len(set(nums[i:j]))**2)
        return sum(ans)
"""
1493. Longest Subarray of 1's After Deleting One Element
Solved
Medium

Topics

Companies

Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution:
    """
    Variant 1:
    My first successful attempt at solving this problem. This solution takes advantage of
    Python's built-in string splitting method, which helps to essentially identify the
    lengths of all subarrays of 'nums' containing only 1. This allows us to solve this
    problem with very little code. My educated (rather confident) guess is that the 
    complexity of this solution is O(n) in both time and space, where n is the length of
    the input array 'nums'. LC's analysis tool confirms these hypotheses. This solution
    beats ~73% and ~38% of accepted answers in terms of RT and memory efficiency
    respectively. 
    """
    def longestSubarray(self, nums: List[int]) -> int:
        nums_str = ''
        for num in nums:
            nums_str += str(num)
        nums_str_list = nums_str.split('0')
        max_len = 0
        if len(nums_str_list) == 1:
            return len(nums_str_list[0]) - 1
        for i in range(len(nums_str_list)-1):
            len_first = len(nums_str_list[i])
            len_second = len(nums_str_list[i+1])
            tot_len = len_first + len_second
            if tot_len > max_len:
                max_len = tot_len

        return max_len

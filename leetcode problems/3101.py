"""
3101. Count Alternating Subarrays
Attempted
Medium
Topics
Companies
Hint
You are given a 
binary array
 nums.

We call a 
subarray
 alternating if no two adjacent elements in the subarray have the same value.

Return the number of alternating subarrays in nums.

 

Example 1:

Input: nums = [0,1,1,1]

Output: 5

Explanation:

The following subarrays are alternating: [0], [1], [1], [1], and [0,1].

Example 2:

Input: nums = [1,0,1,0]

Output: 10

Explanation:

Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.

 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution:
    """
    Variant 1:
    The first solution I came up with to solve this problem. It passes 758/789 tests before
    failing with a 'Time Limit Exceeded' error on Test 759. So I am pretty confident that
    this this would be the 'Brute Force Approach' method to solving this problem but would
    probably not impress in a technical interview. I believe that the time complexity of
    this solution is O(n^3) where n is the length of 'nums', since for each iteration of
    the while loop we have to check if the current element of the subarray of length
    start_len = ~n/2 (on average) in question is equal to its neighbor, and there are 
    len(nums) - start_len + 1 = ~n/2 (on average)
    subarrays we need to look at, len(nums) - 1 = ~n times. So in the worst case the number
    of checks required is between n^2 and n^3, so we will say the time complexity is O(n^3).
    I am not certain of this though, and LC is unable to analyze my submission bc of the
    TLE Error. I believe this solution has space complexity O(1) since the amount of memory
    required for the variables used in this solution does not depend on n. 
    """
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        num_alternating = start_len = len(nums)
        while start_len > 1:
            for start in range(len(nums)-start_len+1):
                alt = True
                sub = nums[start:start+start_len]
                for i in range(len(sub)-1):
                    if sub[i+1] == sub[i]:
                        alt = False
                        break
                if alt:
                    num_alternating += 1
            start_len -= 1
        
        return num_alternating


class Solution:
    """
    Variant 2:
    My first accepted submission to solve this problem. It utilizes the fact that as we
    loop over elements of 'nums', if we are currently extending an alternating subarray
    by 1 element, the increase in the number of subarrays present in 'nums' will be equal
    to the length of the subarray after extending, else the increase will be 1 since the
    subarray containing only the new element is alternating. The time complexity of this 
    solution is O(n) where n is the length of 'nums' and the space complexity is O(1), 
    both figures confirmed by LC's analysis tool. This solution beats ~60% and ~67% of
    accepted answers in terms of RT and memory efficiency.
    """
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        acc = curr_len = 1
        if len(nums) == 1:
            return acc
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                curr_len += 1
            else:
                curr_len = 1
            acc += curr_len
        
        return acc
"""
2032. Two Out of Three
Solved
Easy
Topics
Companies
Hint
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.
 

Example 1:

Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.
Example 2:

Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.
Example 3:

Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.
 

Constraints:

1 <= nums1.length, nums2.length, nums3.length <= 100
1 <= nums1[i], nums2[j], nums3[k] <= 100
"""


class Solution:
    """
    Variant 1:
    Had to get the blood flowing today with an easy one. I was able to come up with this
    solution on my first attempt in less than 5 mins and it beats ~65% and ~55% of accepted
    answers in run time and memory efficiency respectively. My guess is that the time
    complexity of this solution is 
    
    O(n1 + n2 + n3), 
    where n1, n2, n3 are the lengths of nums1, nums2, nums3 respectively, 
    O(n1 + n2 + n3) can be thought of as being proportional to the max of
    these three lengths

    and that the space complexity is also O(n1 + n2 + n3) or O(max(n1,n2,n3)). 

    LC's analysis tool confirms my suspicions. 

    Thumbs up!
    """
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        values = {}
        for num_list in [nums1, nums2, nums3]:
            for ele in set(num_list):
                if ele not in values:
                    values[ele] = 1
                else:
                    values[ele] += 1

        ret = []
        for ele in values.keys():
            if values[ele] > 1:
                ret.append(ele)
        
        return ret
"""
88. Merge Sorted Array
Easy

Topics

Companies

Hint
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""


class Solution:
    """
    Variant 1:
    My first successful attempt at solving this problem on my own. I am guessing that
    the run time complexity of this solution is O(n*(m+n)) sine we have a for loop that
    has n (the length of nums2) iterations, and in that for loop we have a while loop
    which can run up to m times but will not on average (the average will be somewhere
    around 2 which we can treat as a constant factor) and then for each iteration of
    the for loop we have to shift (n+m - pointer + 1) elements in nums1 to the right
    by 1 position. I am guessing that the space complexity of this solution is O(1)
    since the amount of additional variables we need to define in memory does not scale
    as a function of the input list lengths, and rather is constant. This solution simply
    relies on creating two integer variables: num_zeros and pointer. Let's see if
    Leetcode's analysis tool will confirm my hypotheses. Leetcode reports O((n+m)(m+n))
    for the run time complexity and O(1) for the memory complexity. So at the very least
    my hypotheses were close. Still, this is not a great solution since it only beats
    ~30% and 13% of accepted answers in terms of run time and memory efficiency
    respectively. 
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer = 0
        num_zeros = n
        for num in nums2:
            while nums1[pointer] < num and (n+m - pointer) > num_zeros:
                pointer += 1
            print(num)
            print(pointer)
            nums1[pointer+1:] = nums1[pointer:n+m-1]
            nums1[pointer] = num
            num_zeros -= 1
            print(nums1)

        return nums1


class Solution:
    """
    Variant 2:
    My first successful attempt at implementing the approach described by Leetcode in its
    solution to this problem, 'Approach 2: Three Pointers (Start From the Beginning)'.
    After seeing the name of this solution I did not read much of its description or any of
    the solution code, since the name pretty much lit a spark in my brain to do the merge
    in O(m+n) time. This implementation should have O(m+n) and O(m) space complexity
    respectively. The analyze feature of Leetcode confirms this is the case. Still, I am
    not terribly impressed by the actual performance of this implementation, since it only
    beats ~6% and 13% of accepted answers respectively.
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1copy = nums1[:m]
        pointer1 = 0
        pointer2 = 0
        i = 0
        while pointer1 < m and pointer2 < n:
            print(pointer2)
            print(pointer1)
            print(nums1)
            if nums1copy[pointer1] < nums2[pointer2]:
                nums1[i] = nums1copy[pointer1]
                pointer1 += 1
            else:
                nums1[i] = nums2[pointer2]
                pointer2 += 1
            
            i += 1
        
        if pointer1 == m:
            nums1[pointer1 + pointer2:] = nums2[pointer2:]
        else:
            nums1[pointer1 + pointer2:] = nums1copy[pointer1:]

            
        return nums1


class Solution:
    """
    Variant 3:
    The official solution given by Leetcode for 'Approach 2: Three Pointers (Start From 
    the Beginning).' This has the same time and space complexity as Variant2 in terms of
    order of magnitude (big O notation), however this is a slightly more optimal approach
    likely because it doesn't use list slicing to create the end of nums1 list when either
    pointer reaches its maximum allowed value, exiting the while loop. This implementation
    instead uses a for loop to iterate over m + n times and if the pointers exceed their 
    designated range, the logic within the for loop will handle that rather than outside
    the while loop in Variant 2. Thus the observable performance is better for this
    solution, beating ~60% and 30% of accepted answers in terms of run time and memory
    efficiency respectively. 
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m]

        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0

        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1


class Solution:
    """
    Variant 4:
    My successful implementation of 'Approach 3: Three Pointers (Start From the End)'
    given by Leetcode without looking at the description or solution itself. This is
    really the same approach as Variants 2 and 3, with O(m+n) and O(m) complexity in 
    time and space respectively, but nums1 is created in the reverse order from largest
    to smallest. This solution beats ~50% and 30% of accepted answers in terms of run
    time and memory efficiency, respectively. 
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m]

        # Read pointers for nums1Copy and nums2 respectively.
        p1 = -1
        p2 = -1
        p = -1

        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        while p > -1*(m+n) -1:
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 < -n or (p1 > (-1*m - 1) and nums1_copy[p1] >= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            
            p -= 1
    
        return nums1


class Solution:
    """
    Variant 5:
    The official solution for 'Approach 3: Three Pointers (Start From the End)' given by
    Leetcode to solve this problem. This is the optimal approach to solve this problem
    since the run time complexity is O(m+n) and the space complexity is O(1), thus
    minimizing both run time and space complexity. This implentation is superior to my
    own attempt (Variant 4) because it achieves O(1) space complexity by not storing a
    copy of nums1. This solution beats ~70% and ~40% of accepted answers in terms of run
    time and memory efficiency respectively. 
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backward through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

"""
2935. Maximum Strong Pair XOR II
Attempted
Hard
Topics
Companies
Hint
You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:

|x - y| <= min(x, y)
You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.

Return the maximum XOR value out of all possible strong pairs in the array nums.

Note that you can pick the same integer twice to form a pair.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: 7
Explanation: There are 11 strong pairs in the array nums: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
The maximum XOR possible from these pairs is 3 XOR 4 = 7.
Example 2:

Input: nums = [10,100]
Output: 0
Explanation: There are 2 strong pairs in the array nums: (10, 10) and (100, 100).
The maximum XOR possible from these pairs is 10 XOR 10 = 0 since the pair (100, 100) also gives 100 XOR 100 = 0.
Example 3:

Input: nums = [500,520,2500,3000]
Output: 1020
Explanation: There are 6 strong pairs in the array nums: (500, 500), (500, 520), (520, 520), (2500, 2500), (2500, 3000) and (3000, 3000).
The maximum XOR possible from these pairs is 500 XOR 520 = 1020 since the only other non-zero XOR value is 2500 XOR 3000 = 636.
 

Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 220 - 1
"""


class Solution:
    """
    Variant 1:
    After reading but prior to testing out Variant 2 below which is straight from ChatGPT
    I tried implementing what I understood to be the methodology for solving this problem
    but alas I get a TLE on test case 237/349. It turns out that Variant 2 also fails on
    that test case but passes the earlier 236. Because of the sort operation but also the 
    utilization of the break it's hard for me to tell which algorithm btwn Variant 1 and 
    2 is technically more efficient. But I do know that this one has a time complexity of
    O(n^2) where n is the length of nums. Thus we need to come up with an algorithm that
    has a time complexity better than O(n^2).

    LC's analysis tool confirms that the time complexity is O(n^2).
    """
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        #nums = sorted(nums)
        max_xor = 0

        n = len(nums)

        for i in range(len(nums)):
            for j in nums[i:n]:
                if abs(j - nums[i]) <= min(nums[i], j):
                    max_xor = max(max_xor, j ^ nums[i])

        return max_xor



class Solution:
    """
    Variant 2:
    TLE on test case 237/349. My educated guess is that this solution also has time
    complexity of O(n^2) even though the usage of sorting and breaking in this algorithm
    likely improves quite a bit on the efficiency of Variant 1. 

    LC's analysis tool confirms that the time complexity is O(n^2).
    """
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        max_xor = 0
        n = len(nums)
        
        for i in range(n):
            x = nums[i]
            for j in range(i, n):
                y = nums[j]
                if abs(x - y) <= min(x, y):
                    max_xor = max(max_xor, x ^ y)
                else:
                    # Since nums is sorted and y is increasing, we can break early
                    break
        
        return max_xor





class Solution:
    """
    Variant 3:
    WIP
    """
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        def return_max_xor_for_strong_reg(nums_list, pointer1, pointer2):
            print("pointer2")
            print(pointer2)
            last_dist = nums_list[pointer2] - nums_list[pointer1]
            print(last_dist)
            max_xor = 0
            while last_dist <= nums_list[pointer1]:
                print("pointer1")
                print(pointer1)
                max_xor = max(max_xor, nums_list[pointer2] ^ nums_list[pointer1])
                new_dist_1 = nums_list[pointer2-1] - nums_list[pointer1]
                new_dist_2 = nums_list[pointer2] - nums_list[pointer1+1]
                if max(new_dist_1, new_dist_2) < max_xor:
                    print("broke")
                    break
                max_xor = max(max_xor, nums_list[pointer2-1] ^ nums_list[pointer1])
                max_xor = max(max_xor, nums_list[pointer2] ^ nums_list[pointer1+1])
                pointer1 += 1
                pointer2 -= 1
                last_dist = nums_list[pointer2] - nums_list[pointer1]

            return max_xor

        nums = sorted(nums)
        n = len(nums)

        left_pointer = 0
        right_pointer = n - 1
        if (nums[right_pointer] - nums[left_pointer]) <= nums[left_pointer]:
            print("inside 1")
            return max_xor_for_strong_reg(nums, left_pointer, right_pointer)

        else:
            print("inside 2")
            print(right_pointer)
            max_xor = 0
            last_dist = nums[right_pointer] - nums[left_pointer]
            print(last_dist)
            while (last_dist) > nums[left_pointer] and last_dist > max_xor:
                print("inside 3")
                left_reg_max_strong_ind = bisect.bisect_left(nums, 2*nums[0])
                right_reg_min_strong_ind = bisect.bisect_right(nums, nums[1]/2)

                print(left_reg_max_strong_ind)
                print(right_reg_min_strong_ind)
                
                max_xor_left = return_max_xor_for_strong_reg(nums, left_pointer, left_reg_max_strong_ind)
                max_xor_right = return_max_xor_for_strong_reg(nums, right_reg_min_strong_ind, right_pointer)

                print(max_xor_left)
                print(max_xor_right)

                max_xor_lr = max(max_xor_left, max_xor_right)
                max_xor = max(max_xor, max_xor_lr)

                left_pointer = left_reg_max_strong_ind
                right_pointer = right_reg_min_strong_ind
                last_dist = nums[right_pointer] - nums[left_pointer]

            return max_xor
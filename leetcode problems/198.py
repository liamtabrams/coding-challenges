"""
198. House Robber
Attempted
Medium

Topics

Companies
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

class Solution:
    """
    Variant 1:
    My first successful attempt at reproducing the solution for 'Approach 1: Recursion
    with Memorization' given by Leetcode. I basically had to review the solution code
    multiple times over the course of 24 hours in order to fully understand/memorize 
    how to correctly implement this first approach. It was not intuitive for me at all
    but I do find the solution to be quite elegant. The official solution for Approach 1
    given by LC is identical to what I have here except the official solution has a 
    redundant line of code within the 'rob' method of Solution that reinitializes self.memo
    to an empty dictionary even though that already happens in the constructor function 
    for Solution. Anyway, the run time complexity of this solution is O(N) where N is the
    length of 'nums', and so is the space complexity since the self.memo dictionary stores
    N key-value pairs, as well as there being additional memory overhead in the call stack
    which has depth of approximately N. This solution beats ~60% and ~45% of accepted
    answers in terms of run time and memory efficiency, respectively.
    """

    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        return self.robFrom(0, nums)
        
    def robFrom(self, i: int, nums: List[int]) -> int:
        if i >= len(nums):
            return 0

        if i in self.memo:
            return self.memo[i]

        ans = max(self.robFrom(i+1, nums), self.robFrom(i+2, nums) + nums[i])

        self.memo[i] = ans

        return ans


 class Solution:
    """
    Variant 2:
    The official solution for 'Approach 1: Recursion with Memorization' given by LC. It's
    identical to Variant 1 except contains redundancy with a duplicate line 'self.memo = {}'.
    The complexity analysis provided by LC is the following:
    
    Complexity Analysis

    Time Complexity: O(N) since we process at most N recursive calls, thanks to caching, and 
    during each of these calls, we make an O(1) computation which is simply making two other 
    recursive calls, finding their maximum, and populating the cache based on that.

    Space Complexity: O(N) which is occupied by the cache and also by the recursion stack. 

    The average performance of this solution as compared to all accepted answers should be
    the same as Variant 1, so beating ~60% and 45% of accepted answers in terms of RT and
    memory efficiency.  
    """

    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:

        self.memo = {}

        return self.robFrom(0, nums)

    def robFrom(self, i, nums):

        # No more houses left to examine.
        if i >= len(nums):
            return 0

        # Return cached value.
        if i in self.memo:
            return self.memo[i]

        # Recursive relation evaluation to get the optimal answer.
        ans = max(
            self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i]
        )

        # Cache for future use.
        self.memo[i] = ans
        return ans


class Solution:
    """
    Variant 3:
    My own attempt at implementing what I think LC has in mind for 'Approach 2: Dynamic
    Programming' without reading the solution code, which should basically be a very
    similar approach to Approach 1 except it uses a for loop instead of recursion to
    work backwards from the last house. The RT complexity of this implementation should
    be O(N) and same with the space complexity, however this algorithmic approach SHOULD
    be slightly more efficient than the recursive-based approaches of Variants 1 and 2.
    This solution beats ~60% and ~50% of accepted answers respectively in terms of RT and
    memory efficiency, suggesting a slight improvement from Variants 1 and 2 in terms of
    observable memory efficiency.
    """
    def rob(self, nums: List[int]) -> int:
        moneyLookupTable = {}
        last_house_ind = len(nums) - 1
        print(last_house_ind)
        moneyLookupTable[last_house_ind] = nums[last_house_ind]
        moneyLookupTable[last_house_ind+1] = 0
        for i in range(last_house_ind-1, -1, -1):
            ans = max(moneyLookupTable[i+1], nums[i] + moneyLookupTable[i+2])
            moneyLookupTable[i] = ans

        return moneyLookupTable[0]


class Solution:
    """
    Variant 4:
    The official solution given by LC for 'Approach 2: Dynamic Programming'. This is very
    similar to the code I came up with on my own in Variant 3, however this solution uses
    a list to cache the maximum robbable amount at each house starting at the last, rather
    than a dictionary. The complexity analysis provided by LC is the following:

    Complexity Analysis

    Time Complexity: O(N) since we have a loop from N-2 to 0 and we simply use the pre-calculated
    values of our dynamic programming table for calculating the current value in the table 
    which is a constant time operation.

    Space Complexity: O(N) which is used by the table. So what is the real advantage of this 
    solution over the previous solution? In this case, we don't have a recursion stack. When 
    the number of houses is large, a recursion stack can become a serious limitation, because
    the recursion stack size will be huge and the compiler will eventually run into 
    stack-overflow problems (no pun intended!).

    To reiterate, implementations using this approach (Variants 3 & 4) are preferable to 
    implementations using the recursive approach (Variants 1 & 2) because not using recursion
    avoids the possibility of eventually running into stack overflow problems if the number
    of houses is large enough. 

    This solution beats about ~60% and 40% of accepted answers in terms of RT and memory
    efficiency. Though my observations of performance metrics for this particular solution
    suggest this implementation may be slightly less efficient than Variant 3, I cannot say
    for sure. I would need to do rigorous testing to be sure.
    """

    def rob(self, nums: List[int]) -> int:

        # Special handling for empty case.
        if not nums:
            return 0

        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)

        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

        # DP table calculations.
        for i in range(N - 2, -1, -1):

            # Same as recursive solution.
            maxRobbedAmount[i] = max(
                maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i]
            )

        return maxRobbedAmount[0]
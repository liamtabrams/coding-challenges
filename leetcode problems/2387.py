"""
2387. Median of a Row Wise Sorted Matrix
Medium

Topics

Companies

Hint
Given an m x n matrix grid containing an odd number of integers where each row is sorted in non-decreasing order, return the median of the matrix.

You must solve the problem in less than O(m * n) time complexity.

 

Example 1:

Input: grid = [[1,1,2],[2,3,3],[1,3,4]]
Output: 2
Explanation: The elements of the matrix in sorted order are 1,1,1,2,2,3,3,3,4. The median is 2.
Example 2:

Input: grid = [[1,1,3,3,4]]
Output: 3
Explanation: The elements of the matrix in sorted order are 1,1,3,3,4. The median is 3.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
m and n are both odd.
1 <= grid[i][j] <= 106
grid[i] is sorted in non-decreasing order.
"""


class Solution:
    """
    Variant 1: My successful reproduction of Jojo's 'Basic Practice - binary search in 
    general paradigm | Python' from the Solutions section. This solution uses a binary
    search method to check whether a given value in the search space is less than the
    median based on how many of the elements of the grid are less than or equal to it.
    Therefore, I would guess that the time complexity of this algorithm is O(m*logn)
    where m is the number of rows and n is the length of each row, assuming the bisect
    operation has a time complexity of logn associated with it, although I am not very
    confident in my guess. I would guess that the space complexity of this algorithm is
    constant or O(1) since we don't have to store any information that scales in memory 
    usage with the grid size. Really there is an additional factor in the time complexity
    of log(10**6 + 1), but that does evaluate to a constant. So my guess on the order of
    the time complexity was correct! At least according to Jojo, who provides the following
    explanation: 

    --------------------------------------------------------------------------------------

    3- Analysis and Time Complexity

    Method: standard binary search

    Idea: we want to find a value minimal s such that there are m * n // 2 + 1
    matrix/grid elements that are less than or equal to s.

    Procedure/Paradigm:

    1- First we write a function fulfull(s) which is boolean and returns
    if there are at least m * n // 2 + 1 elements in grid that are <= s

    2- We use binary search to find minimal such s.

    For this paradigm of binary search, please check out the binary search playlist
    to see more explanations, deeper details and applications.

    The interesting point here is that: for step 1- above, we can also use binary search. The reason is simple: each row of the matrix is sorted. As such, we can
    use binary search to check how many items in each row are <= s, then add them together to get the number of items in the whole matrix that are <= s.

    given a row, say [1,1,2], we can use bisect_right to get how many items in it
    that are <= s,

    for example, bisect_right([1, 1, 2], 1) is 2; bisect_right([1, 1, 2], 2) is 3;
    bisect_right([1, 1, 2], 3) is 3.

    Time Complexity:

    m * log(n) * log(10 ** 6 + 1 - 0 ) <~ m * log(n) * log(10 ** 6)
    <~ m * log(n) * 6 * log(10) <~ m * log(n) * 6 * 4 <~ m * log(n)
    
    --------------------------------------------------------------------------------------

    LC's analysis tool claims that the time complexity is actually O(m*n*log(10^6)). But
    I really don't think that's correct... It does agree with me that the space complexity
    is O(1) though. This solution beats ~93% and ~40% of accepted answers in terms of RT
    and memory efficiency respectively.
    """
    def matrixMedian(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def check_if_lt_median(val):
            res = 0
            for row in grid:
                res += bisect.bisect_right(row, val)
            
            return res >= m*n // 2 + 1
    
        left, right = 0, 10**6 + 1

        while left < right:
            mid = left + (right - left)//2

            if check_if_lt_median(mid):
                right = mid
            else:
                left = mid + 1

        return left
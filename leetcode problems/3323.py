"""
3323. Minimize Connected Groups by Inserting Interval
Solved
Medium

Topics

Companies

Hint
You are given a 2D array intervals, where intervals[i] = [starti, endi] represents the start and the end of interval i. You are also given an integer k.

You must add exactly one new interval [startnew, endnew] to the array such that:

The length of the new interval, endnew - startnew, is at most k.
After adding, the number of connected groups in intervals is minimized.
A connected group of intervals is a maximal collection of intervals that, when considered together, cover a continuous range from the smallest point to the largest point with no gaps between them. Here are some examples:

A group of intervals [[1, 2], [2, 5], [3, 3]] is connected because together they cover the range from 1 to 5 without any gaps.
However, a group of intervals [[1, 2], [3, 4]] is not connected because the segment (2, 3) is not covered.
Return the minimum number of connected groups after adding exactly one new interval to the array.

 

Example 1:

Input: intervals = [[1,3],[5,6],[8,10]], k = 3

Output: 2

Explanation:

After adding the interval [3, 5], we have two connected groups: [[1, 3], [3, 5], [5, 6]] and [[8, 10]].

Example 2:

Input: intervals = [[5,10],[1,1],[3,3]], k = 1

Output: 3

Explanation:

After adding the interval [1, 1], we have three connected groups: [[1, 1], [1, 1]], [[3, 3]], and [[5, 10]].

 

Constraints:

1 <= intervals.length <= 105
intervals[i] == [starti, endi]
1 <= starti <= endi <= 109
1 <= k <= 109
"""


class Solution:
    """
    Variant 1:
    I got this solution, 'Sort + Merge + Sliding Window (no need for binary search)' from 
    zwzbill8, from this problem's Solutions section. Though it was a bit difficult to
    follow at first, this is a reasonable and rather efficient methodology to solving the
    problem. First the total number of groups in the input is computed with the merge
    function. Then, the number of other groups we can connect with an interval of length k 
    starting at the endpoint of a given group is calculated for each group, and the maximum 
    (or in this case minimum - since we increment with -1 not 1) number of groups that can be 
    connected after taking into account all these covering locations is subtracted from the
    initial number of groups we computed by taking the length of the result returned by merge(). 
    Anyway, this is a rather straightforward and elegant way to solve this problem. 

    I attempted solving this problem on my own for about an hour, and what I came up with got 
    close to passing all test cases but never fully solved the problem and was incredibly
    inefficient. But I will test myself again on this problem in the future.

    My educated guess is that the time complexity of this solution is technically O(N^2) where
    N is the length of the input list intervals and that the space complexity is O(1). 

    LC's analysis tool disagrees however, and claims that the time and space complexity are O(NlogN) 
    and O(N) respectively. The time complexity seems a bit harder for me to generalize or explain,
    but LC's claim that the space complexity is O(N) seems questionable, considering the input 
    variable 'intervals' gets reassinged to store the group intervals and we don't declare new
    variables who will have their required memory scale with the input. However, I believe a new
    list has to be created in memory when intervals.sort() is called, and that might be what is
    causing the space complexity to be O(N) although I am just guessing.

    This solution beats ~40% and ~35% of accepted answers in terms of RT and memory efficiency,
    respectively.   
    """
    def minConnectedGroups(self, intervals: List[List[int]], k: int) -> int:
        intervals.sort()
    
        def merge(intervals):
            res = []
            for s, e in intervals:
                if res and res[-1][1] >= s:
                    res[-1][1] = max(res[-1][1], e)
                else:
                    res.append([s, e])
            return res
    
        intervals = merge(intervals)
        
        groups = len(intervals)
        res = groups

        j = 0
        for _, e in intervals:
            while j < len(intervals) and e + k >= intervals[j][0]:
                groups -= 1
                j += 1
            groups += 1  # include the first interval
            res = min(res, groups)
        return res
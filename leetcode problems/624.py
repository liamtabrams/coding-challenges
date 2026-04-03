"""

Code
Testcase
Test Result
Test Result
624. Maximum Distance in Arrays
Attempted
Medium
Topics
conpanies icon
Companies
You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

 

Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0
 

Constraints:

m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.
"""

class Solution(object):
    """
    Variant 1:
    My first attempt at solving this problem. This resulted in a "Wrong Answer", but I wanted
    to include it here because it passed 39/136 of the test cases with somewhat intuitive logic,
    though that logic is rather messy/unelegant. The goal is to now figure out what the missed
    edge case is and see if this approach works well in terms of run time. 
    """
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        mins = []
        maxes = []
        curr_ind = 0
        curr_min = 10**4
        curr_max = -(10**4)
        curr_diff = 0
        for array in arrays:
            array_min = array[0]
            array_max = array[-1]
            mins.append(array_min)
            maxes.append(array_max)
            min_diff = 0
            max_diff = 0
            if array_min < curr_min:
                min_diff = curr_min - array_min
            if array_max > curr_max:
                max_diff = array_max - curr_max

            if curr_ind == 1:
                curr_diff = max(maxes[1] - mins[0], maxes[0] - mins[1])
            if curr_ind > 1:
                curr_diff_inc = max(min_diff, max_diff)
                curr_diff += curr_diff_inc 
            curr_ind += 1

        return curr_diff
        

class Solution(object):
    """
    Variant 2:
    We caught the first bug in our code which was due to not updating the values of curr_min
    and curr_max in our for loop where it was necessary. It's surprising that the code in
    Variant 1 passed so many test cases. Now this code is passing 95/136 test cases, where
    the remaining failed test cases may be more obscure. I'm going to try to understand
    why those are failing now. 
    """
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        mins = []
        maxes = []
        curr_ind = 0
        curr_min = 10**4
        curr_max = -(10**4)
        curr_diff = 0
        for array in arrays:
            array_min = array[0]
            array_max = array[-1]
            mins.append(array_min)
            maxes.append(array_max)
            min_diff = 0
            max_diff = 0
            if array_min < curr_min:
                min_diff = curr_min - array_min
                curr_min = array_min
            if array_max > curr_max:
                max_diff = array_max - curr_max
                curr_max = array_max
            if curr_ind == 1:
                curr_diff = max(maxes[1] - mins[0], maxes[0] - mins[1])
            if curr_ind > 1:
                curr_diff_inc = max(min_diff, max_diff)
                curr_diff += curr_diff_inc 
            curr_ind += 1

        return curr_diff


class Solution(object):
    """
    Variant 3: 
    I made a rather rough attempt at a bug fix for the code in Variant 2 the result of which
    passes fewer test cases, at 73/136. Clearly I need to take a step back. 
    """
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        mins = []
        maxes = []
        curr_ind = 0
        curr_min = 10**4
        curr_max = -(10**4)
        curr_diff = 0
        for array in arrays:
            array_min = array[0]
            array_max = array[-1]
            mins.append(array_min)
            maxes.append(array_max)
            min_diff = 0
            max_diff = 0
            if array_min < curr_min:
                min_diff = curr_min - array_min
            if array_max > curr_max:
                max_diff = array_max - curr_max
            if curr_ind == 1:
                if maxes[1] - mins[0] >= maxes[0] - mins[1]:
                    curr_min = mins[0]
                    curr_max = maxes[1]
                else:
                    curr_min = mins[1]
                    curr_max = maxes[0]
                
                curr_diff = max(maxes[1] - mins[0], maxes[0] - mins[1])

            if curr_ind > 1:
                if max_diff >= min_diff:
                    curr_max = array_max
                else:
                    curr_min = array_min
                curr_diff_inc = max(min_diff, max_diff)
                curr_diff += curr_diff_inc 
            curr_ind += 1
            print(curr_diff)
            print(curr_ind)

        return curr_diff

        

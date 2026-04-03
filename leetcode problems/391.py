"""
391. Perfect Rectangle
Solved
Hard

Topics

Companies
Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

Return true if all the rectangles together form an exact cover of a rectangular region.

 

Example 1:


Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
Output: true
Explanation: All 5 rectangles together form an exact cover of a rectangular region.
Example 2:


Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
Output: false
Explanation: Because there is a gap between the two rectangular regions.
Example 3:


Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
Output: false
Explanation: Because two of the rectangles overlap with each other.
 

Constraints:

1 <= rectangles.length <= 2 * 104
rectangles[i].length == 4
-105 <= xi < ai <= 105
-105 <= yi < bi <= 105
"""


class Solution:
    """
    Variant 1:
    This is '[Python] Fast and clear solution with explanation' from Seint which I got
    from the Solutions section. Not only is this approach to solving this problem 
    incredibly clever and elegant, but the presentation of the code itself is rather
    advanced, particularly with how they define and evaluate distance and area using lambda 
    functions. The scoping of the variables x, X, y, and Y within the 'isRectangleCover'
    function is particularly interesting with how the 'a' function gets automatically 
    evaluated on them. This is like 10 yr Python developer code that solves the same problem
    an intermediate Python programmer might solve in 20 more lines of code. Basically this
    code belongs in a museum.

    Anyway, my educated guess is that the time and space complexity of this solution are
    both O(n) where n is the length of 'rectangles'. However if this algorithm returns True
    then that means it only had to store 4 corners in the end so it will only be O(n) for the space
    complexity in the worst case. LC's analysis tool agrees with my hypotheses. This solution beats
    ~84% and ~56% of accepted answers in terms of run time and memory efficiency respectively.
    """
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        area = 0
        corners = set()
        a = lambda: (Y-y) * (X-x)
        
        for x, y, X, Y in rectangles:
            area += a()
            corners ^= {(x,y), (x,Y), (X,y), (X,Y)}

        if len(corners) != 4: return False
        x, y = min(corners, key=lambda x: x[0] + x[1])
        X, Y = max(corners, key=lambda x: x[0] + x[1])
        return a() == area
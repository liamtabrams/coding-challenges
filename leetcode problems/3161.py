"""
3161. Block Placement Queries
Attempted
Hard
Topics
Companies
Hint
There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

You are given a 2D array queries, which contains two types of queries:

For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

 

Example 1:

Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]

Output: [false,true,true]

Explanation:



For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

Example 2:

Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]

Output: [true,true,false]

Explanation:



Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.
 

Constraints:

1 <= queries.length <= 15 * 104
2 <= queries[i].length <= 3
1 <= queries[i][0] <= 2
1 <= x, sz <= min(5 * 104, 3 * queries.length)
The input is generated such that for queries of type 1, no obstacle exists at distance x when the query is asked.
The input is generated such that there is at least one query of type 2.
"""

class Solution:
    """
    Variant 1:
    The first implementation I wrote that I THINK "TECHNICALLY" solves the problem except 
    it runs into a Time Limit Exceeded Error on LC. I believe that the time complexity of
    this particular implementation is O(n^2) where n is the length of queries, though in
    the average case the number of nested for loop iterations would come out to about 
    (n/(2*2))*(n/2) = (n^2)/8 + (n*(log(n^(1/2)))/2) = ~(n^2)/8 as n gets large and we 
    assume an even distribution of type 1 and type 2 queries. The space complexity of this 
    solution would be O(n). We need to work off of this approach to find a solution that 
    runs in an acceptable amount of time.
    """
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obstacles = []
        results = []

        for query in queries:
            if query[0] == 1:
                obstacles.append(query[1])
                obstacles = sorted(obstacles)
                continue
            val = False
            last_ob = 0
            if not len(obstacles) and query[2] <= query[1]:
                val = True
            for i in range(len(obstacles)):
                if obstacles[i] <= query[1]:
                    if obstacles[i] - last_ob >= query[2]:
                        val = True
                        break
                    last_ob = obstacles[i]
                else:
                    break
            if query[1] - last_ob >= query[2]:
                val = True
            results.append(val)

        return results
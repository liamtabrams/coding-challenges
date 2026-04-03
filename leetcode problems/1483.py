"""
1483. Kth Ancestor of a Tree Node
Attempted
Hard
Topics
Companies
Hint
You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of ith node. The root of the tree is node 0. Find the kth ancestor of a given node.

The kth ancestor of a tree node is the kth node in the path from that node to the root node.

Implement the TreeAncestor class:

TreeAncestor(int n, int[] parent) Initializes the object with the number of nodes in the tree and the parent array.
int getKthAncestor(int node, int k) return the kth ancestor of the given node node. If there is no such ancestor, return -1.
 

Example 1:


Input
["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
[[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
Output
[null, 1, 0, -1]

Explanation
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor
 

Constraints:

1 <= k <= n <= 5 * 104
parent.length == n
parent[0] == -1
0 <= parent[i] < n for all 0 < i < n
0 <= node < n
There will be at most 5 * 104 queries.
"""

class TreeAncestor:
    """
    Variant 1:
    This solution was posted by Ye Gao and can be viewed at:
    https://leetcode.com/problems/kth-ancestor-of-a-tree-node/solutions/686482/python3-binary-lifting-dp/.

    It is a rather elegant solution to this problem which leverages binary lifting. 

    Before referring to more trustworthy complexity analysis, I am guessing that the time complexity of
    this solution is O(nlogn), because, looking at the nested for loops in the __init__ function, for 
    each value of m (which scales as log2(n)), we need to iterate over every single node in the tree to
    generate the desired matrix values. I believe this will dominant the time complexity. I'm guessing
    that similarly the __init__ function will dominate the space complexity which contributes O(nlogn)
    space complexity as well. According to LC's analysis tool, my hypotheses are correct! 


    Compared to other submissions, this solution performs quite well, beating ~70% of ~65% of accepted
    answers in terms of RT and memory efficiency.
    """
    def __init__(self, n: int, parent: List[int]):
        m = 1 + int(log2(n)) #at most 16 for this problem 
        self.dp = [[-1] * m for _ in range(n)] #ith node's 2^j parent
        for j in range(m):
            for i in range(n):
                if j == 0: self.dp[i][0] = parent[i] #2^0 parent
                elif self.dp[i][j-1] != -1: 
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
    
    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1: 
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node 
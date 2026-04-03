"""
1766. Tree of Coprimes
Attempted
Hard
Topics
Companies
Hint
There is a tree (i.e., a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. Each node has a value associated with it, and the root of the tree is node 0.

To represent this tree, you are given an integer array nums and a 2D array edges. Each nums[i] represents the ith node's value, and each edges[j] = [uj, vj] represents an edge between nodes uj and vj in the tree.

Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the greatest common divisor of x and y.

An ancestor of a node i is any other node on the shortest path from node i to the root. A node is not considered an ancestor of itself.

Return an array ans of size n, where ans[i] is the closest ancestor to node i such that nums[i] and nums[ans[i]] are coprime, or -1 if there is no such ancestor.

 

Example 1:



Input: nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
Output: [-1,0,0,1]
Explanation: In the above figure, each node's value is in parentheses.
- Node 0 has no coprime ancestors.
- Node 1 has only one ancestor, node 0. Their values are coprime (gcd(2,3) == 1).
- Node 2 has two ancestors, nodes 1 and 0. Node 1's value is not coprime (gcd(3,3) == 3), but node 0's
  value is (gcd(2,3) == 1), so node 0 is the closest valid ancestor.
- Node 3 has two ancestors, nodes 1 and 0. It is coprime with node 1 (gcd(3,2) == 1), so node 1 is its
  closest valid ancestor.
Example 2:



Input: nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
Output: [-1,0,-1,0,0,0,-1]
 

Constraints:

nums.length == n
1 <= nums[i] <= 50
1 <= n <= 10^5
edges.length == n - 1
edges[j].length == 2
0 <= uj, vj < n
uj != vj
"""

class Solution:
    """
    Variant 1:
    The solution provided by Happy Coding on YouTube at https://www.youtube.com/watch?v=DMGtWgH5VmU.
    As explained in the video, the constraints given in this problem allow for us to find a
    specialized approach to optimize for time efficiency. Prior to reviewing the video's discussion of
    complexity, my guess is that the time complexity of this solution would be O(n) where n = len(nums)
    based on how the implementation looks and the fact that the video mentions we are trying to do
    better than O(n^2). However that is still just an educated guess. According to the video though, the
    time complexity in the worst case is n*50*log50 which is ~ O(n). The 50*n factor of the expression 
    comes from the fact that for each of the n nodes we do a for loop over parents which can have at most 
    50 elements. The log50 factor comes from the sorting of at most 50 items in parent list. We can do 
    this because we cleverly identified that for this problem there are only at most 50 possible node 
    tuples in each node's parent dictionary despite there being up to 10^5 nodes in the tree (since for 
    any given node's family history we only care about the most recent depth for a given value). Also
    according to the video, the space complexity of this solution in the worst case is n*50 because, 
    looking at the parents dictionary list, we have n dictionaries which will have at most 50 key-value
    pairs. Thus, the space complexity should be O(n). 

    According to the measurable efficiency metrics on LC, this solution beats only about 7% of accepted
    answers for both time and memory efficiency. This means there are likely much better solutions out
    there.


    The solution presenter states that for this problem, the idea is not THAT hard but the challenge is
    rather implementation heavy. One of the main challenges is figuring out how to correctly gather the
    needed parent node information using the DFS algorithm by using valid data structures and having them
    flow correctly through the recursion stack.
    """
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        def gcd(a, b):
            while b:
                a, b = b, a % b

            return a

        def dfs(cur, pathDict, depth):
            parents[cur] = pathDict.copy()
            seen.add(cur)
            newPathDict = pathDict.copy()
            newPathDict[nums[cur]] = (depth, cur)
            for child in graph[cur]:
                if child not in seen:
                    dfs(child, newPathDict, depth+1)

        n = len(nums)
        '''for the following dictionaries stored in parents:
        the keys are the values of the ancestor node, and the values are the maximum 
        depth of node with that value'''
        parents = [{}] * n
        graph = defaultdict(list)
        '''as stated in the video, since the u and v are not guaranteed to represent a parent- 
        child relationship we have to create an undirected graph'''
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # populate parents, we need to do a DFS
        '''since we are dealing with an undirected graph, we need to maintain a 'seen' set
        to eventually break out of the DFS recursion'''
        seen = set()
        # initialize DFS algorithm at starting 0, with an empty pathDict, at a current depth of 0
        dfs(0, {}, 0)

        # generate ans
        ans = []
        for i in range(len(nums)):
            num1 = nums[i]
            parentsList = [(depth, key, nodeId) for key, (depth, nodeId) in parents[i].items()] 
            parentsList.sort(reverse=True)

            node = -1

            for _, num2, nodeId in parentsList:
                if gcd(num1, num2) == 1:
                    node = nodeId
                    break
            
            ans.append(node)

        return ans 


class Solution:
    """
    Variant 2:
    The following solution is from Mai Thanh Hiep and can be seen at
    https://leetcode.com/problems/tree-of-coprimes/solutions/1074737/python-3-dfs-clean-concise/.
    This solution is slightly better than Variant 1 in terms of measurable efficiency,
    particularly when it comes to memory, beating ~8% and ~40% of accepted answers in terms of
    run time and memory efficiency respectively.
    """
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        ans = [-1] * len(nums)
        path = [[] for _ in range(51)]
        graph = defaultdict(list)
        seen = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, depth):
            if node in seen: return
            seen.add(node)
            largestDepth = -1
            for x in range(1, 51):
                if gcd(nums[node], x) == 1: # co-prime
                    if len(path[x]) > 0:
                        topNode, topDepth = path[x][-1]
                        if largestDepth < topDepth:  # Pick node which has largestDepth and co-prime with current node as our ancestor node
                            largestDepth = topDepth
                            ans[node] = topNode
            path[nums[node]].append((node, depth))
            for nei in graph[node]:
                dfs(nei, depth + 1)
            path[nums[node]].pop()

        dfs(0, 0)
        return ans
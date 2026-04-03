"""
133. Clone Graph
Solved
Medium

Topics

Companies
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
 

Constraints:

The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from typing import Optional
class Solution:
    """
    Variant 1:
    My first successful attempt at reproducing 'Approach 2: Breadth First Search' given
    by LC for solving this problem. BFS/queueing was instinctually what came to my mind when
    I first attempted to solve this problem, however what LC actually wanted in terms of all
    nodes being copied and stored in the 'visited' dictionary wasn't successfully implemented
    by me until after looking at the official solution and debugging my implementation multiple 
    times. Since this method was the most intuitive for me I decided to try implementing 
    Approach 2 for myself as Variant 1. I am having trouble understanding why, but the time
    complexity of this solution as well as Variant 2 is O(V+E) where V is the number of nodes
    and E is the number of edges connecting nodes in the graph. According to the Editorial
    section, the BFS-based approach has space complexity O(V), since space is occupied by the 
    visited dictionary and in addition to that, space would also be occupied by the queue 
    since we are adopting the BFS approach here. The space occupied by the queue would be equal
    to O(W) where W is the width of the graph. Overall, the space complexity would be O(N), 
    since W is bounded by N. This particular solution beats ~66% and ~40% of accepted answers
    in terms of RT and memory efficiency respectively.
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visited = {}
        visited[node] = Node(node.val, [])
        queue = deque([node])
        while queue:
            n = queue.popleft()
            for neighb in n.neighbors:
                if neighb not in visited:
                    visited[neighb] = Node(neighb.val, [])
                    queue.append(neighb)
                visited[n].neighbors.append(visited[neighb])

        return visited[node]


from collections import deque
class Solution:
    """
    Variant 2:
    The official solution for 'Approach 2: Breadth First Search' given by LC for solving
    this problem. I don't have compelling evidence, but this implementation seems to perform
    slightly worse in terms of RT efficiency and slightly better in terms of memory efficiency
    than Variant 1, beating ~50% of accepted answers in both categories. 
    """
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]
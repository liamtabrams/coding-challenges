"""
1926. Nearest Exit from Entrance in Maze
Attempted
Medium

Topics

Companies

Hint
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
 

Constraints:

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.
"""


class Solution:
    """
    Variant 1:
    The solution I have submitted that has passed the most test cases thus far (157/194).
    However, I run into a 'Time Limit Exceeded' Error on test case 158. I am guessing that
    this particular solution has O(m*n) complexity in both time and space, but I am not
    certain. I will have to look at the official solution given by LC and compare this to
    it in order to get a better idea of whether that is an accurate assessment. 
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        queue = deque()
        queue.append([entrance[0], entrance[1], 0])
        visited = []
        while queue:
            row, col, steps = queue.popleft()
            print(row)
            print(col)
            print(steps)
            if [row, col] not in visited:
                if row > 0:
                    if maze[row-1][col] == '.' and [row-1, col] not in visited:
                        if row-1 == 0 or col in [0, n-1]:
                            return steps + 1
                        else:
                            queue.append([row-1, col, steps+1])
                if row < m - 1 and [row+1, col] not in visited:
                    if maze[row+1][col] == '.':
                        if row+1 == m-1 or col in [0, n-1]:
                            return steps + 1
                        else:
                            queue.append([row+1, col, steps+1])
                if col < n - 1 and [row, col+1] not in visited:
                    if maze[row][col + 1] == '.':
                        if row in [0, m-1] or col+1 == n-1:
                            return steps + 1
                        else:
                            queue.append([row, col+1, steps+1])
                if col > 0 and [row, col-1] not in visited:
                    if maze[row][col - 1] == '.':
                        if row in [0, m-1] or col-1 == 0:
                            print('returning steps')
                            return steps + 1
                        else:
                            queue.append([row, col-1, steps+1])

            visited.append([row, col])

        return -1


class Solution:
    """
    Variant 2:
    Modification of Variant 1 to pass all test cases after referring to the official
    solution given by LC. This is effectively just the LC solution. The key to getting my 
    code to satisfy LC's run time and memory constraints was to mark previously visited
    cells with '+' so we don't visit them again. According to LC's editiorial section,
    the time complexity of the official solution is O(m*n), which is somewhat intuitive,
    and the space complexity is O(max(m,n)) which is less intuitive. Here is the full
    explanation:

    ---------------------------------------------------------------------------------------

    Time complexity: O(m⋅n)

    For each visited cell, we add it to queue and pop it from queue once, which takes 
    constant time as the operation on queue requires O(1) time. For each cell in queue, we
    mark it as visited in maze, and check if it has any unvisited neighbors in all four 
    directions. This also takes constant time. In the worst-case scenario, we may have to 
    visit O(m⋅n) cells before the iteration stops. To sum up, the overall time complexity 
    is O(m⋅n).
    
    Space complexity: O(max(m,n))

    We modify the input matrix maze in-place to mark each visited cell, it requires constant 
    space. We use a queue queue to store the cells to be visited. In the worst-case scenario, 
    there may be O(m+n) cells stored in queue. The space complexity is O(m+n) + O(max(m,n)).

    ---------------------------------------------------------------------------------------

    This particular solution beats ~80% and ~35% of accepted answers in terms of RT and
    memory efficiency respectively.
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque()
        queue.append([entrance[0], entrance[1], 0])
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            row, col, steps = queue.popleft()
            #print(row)
            #print(col)
            #print(steps)
            for d in dirs:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0 <= new_row <= m-1 and 0 <= new_col <= n-1:
                    if maze[new_row][new_col] == '.':
                        if new_row in [0, m-1] or new_col in [0, n-1]:
                            return steps + 1
                        else:
                            queue.append([new_row, new_col, steps+1])
                            maze[new_row][new_col] = '+'

        return -1


class Solution:
    """
    Variant 3:
    The official solution given by LC for this problem. It's the methodology that Variant
    2 is based on, so refer to the docstring for Variant 2 for an explanation of the time
    and space complexity. This implementation does not have an obvious difference in terms
    of efficiency from Variant 2, beating ~80% and ~35% of accepted answers in terms of run
    time and memory usage respectively.   
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        # Mark the entrance as visited since its not a exit.
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        
        # Start BFS from the entrance, and use a queue `queue` to store all 
        # the cells to be visited.
        queue = collections.deque()
        queue.append([start_row, start_col, 0])
        
        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()
            
            # For the current cell, check its four neighbor cells.
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]
                
                # If there exists an unvisited empty neighbor:
                if 0 <= next_row < rows and 0 <= next_col < cols \
                    and maze[next_row][next_col] == ".":
                    
                    # If this empty cell is an exit, return distance + 1.
                    if 0 == next_row or next_row == rows - 1 or 0 == next_col or next_col == cols - 1:
                        return curr_distance + 1
                    
                    # Otherwise, add this cell to 'queue' and mark it as visited.
                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])
            
        # If we finish iterating without finding an exit, return -1.
        return -1

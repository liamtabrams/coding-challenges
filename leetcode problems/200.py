"""
200. Number of Islands
Solved
Medium

Topics

Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    """
    Variant 1:
    My first successful attempt at solving this problem, which is basically just me copying
    'Approach 2: BFS' solution provided by leetcode. On previous attempts I thought I had 
    correctly implemented the BFS algorithm for solving this problem but leetcode found 
    that my code took to long to run. As it turns out, I had a subtle mistake in my code 
    where I marked the land cell as visited by changing its value to "0" only after popping
    its coordinates from 'neighbors', rather than doing it as soon as the coordinate tuple 
    is appended to 'neighbors'. This resulted in the same cells being repeatedly appended 
    to 'neighbors' which is why I ran into the Time Limit Exceeded error. The run time 
    complexity for this particular solution is O(MxN) where M and N are the dimensions of
    the grid. The space complexity is also O(MxN), since we require the 'grid' data 
    structure, the 2D list with dimensions M and N, to keep track of which land cells have 
    been visited and which have not. There are other variables/data structures defined in 
    this code, but 'grid' is the dominant one. This particular solution beat ~ 92% and 80% 
    of accepted answers in terms of run time and memory efficiency, respectively. 
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0
        for row in range(nr):
            for col in range(nc):
                if grid[row][col] == "1":
                    num_islands+=1
                    grid[row][col] = "0"
                    neighbors = []
                    neighbors.append((row,col))
                    while neighbors:
                        new_row, new_col = neighbors.pop(0)
                        if new_row + 1 < nr and grid[new_row+1][new_col] == "1":
                            neighbors.append((new_row+1, new_col))
                            grid[new_row + 1][new_col] = "0"
                        if new_row - 1 >= 0 and grid[new_row-1][new_col] == "1":
                            neighbors.append((new_row-1, new_col))
                            grid[new_row - 1][new_col] = "0"
                        if new_col - 1 >= 0 and grid[new_row][new_col-1] == "1":
                            neighbors.append((new_row, new_col-1))
                            grid[new_row][new_col - 1] = "0"
                        if new_col + 1 < nc and grid[new_row][new_col+1] == "1":
                            neighbors.append((new_row, new_col+1))
                            grid[new_row][new_col + 1] = "0"

        return num_islands

class Solution:
    """
    Variant 2:
    This is my successful reproduction of the DFS-based approach used to solve this.
    Being able to successfully implement the BFS-based solution allowed me to implement
    this one with relative ease and without referring to the solution provided by 
    leetcode for DFS. Just like Variant 1 (BFS), this solution has O(MxN) RT and space
    complexity as it iterates over every row and column of the grid (nested for loop),
    and uses the exact same data structures as Variant 1. This particular solution beat
    ~ 90% and 70% of accepted answers in terms of RT and memory efficiency respectively,
    and is maybe slightly less efficient, particularly space-wise, than the BFS approach.
    Why might that be?
    
    Well, for one, use of a recursive call stack has additional memory overhead
    associated with it.

    Time-wise, the checking of each cell's vertical and horizontal neighbors should be
    equivalent for the DFS and BFS. So, why might our observations suggest that this
    particular implementation (DFS) is slightly slower than BFS? I suspect that there
    is additional latency associated with accessing items from the call stack.

    In short, this particular approach (DFS) is less efficient than Variant 1 (BFS)
    because it uses a call stack which adds time and space complexity to the solution.
    Otherwise, BFS and DFS would have the same average performance for both time and
    memory efficiency. 
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0
        def find_neighboring_lands(neighbors):
            while neighbors:
                row, col = neighbors.pop(-1)
                if row + 1 < nr and grid[row+1][col] == "1":
                    grid[row+1][col] = "0"
                    neighbors.append((row+1,col))
                if row - 1 >= 0 and grid[row-1][col] == "1":
                    grid[row-1][col] = "0"
                    neighbors.append((row-1,col))
                if col + 1 < nc and grid[row][col+1] == "1":
                    grid[row][col+1] = "0"
                    neighbors.append((row,col+1))
                if col - 1 >= 0 and grid[row][col-1] == "1":
                    grid[row][col-1] = "0"
                    neighbors.append((row,col-1))
                return find_neighboring_lands(neighbors)
            return 
        
        for row in range(nr):
            for col in range(nc):
                if grid[row][col] == "1":
                    num_islands+=1
                    grid[row][col] = "0"
                    neighbors = []
                    neighbors.append((row, col))
                    find_neighboring_lands(neighbors)

        return num_islands


class UnionFind:
    def __init__(self, grid):
        self.count = 0
        self.rank = []
        self.parent = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i*n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)


    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1
        
    def get_count(self):
        return self.count

class Solution:
    """
    Variant 3:
    This is essentially me copying the solution given by leetcode: 'Approach #3: Union 
    Find (aka Disjoint Set)', which defines a custom data structure UnionFind and then
    numIslands function which uses this data structure to count all disjoint sets in
    the grid (not including the 'water' set). The run time complexity of this particular
    implementation is again O(MxN), and so is the space complexity. However, looking at
    the code as well as performance metrics quickly suggest that this is an inferior
    approach to Variants 1 & 2. Note the extra nested MxN for loop that has to execute in
    order to initialize the UnionFind data structure, as well as the additional variables/
    attributes defined in its class definition. These are primary reasons why this
    particular implementation beats only ~26% and ~43% of accepted answers in terms of run
    time and memory efficiency, respectively. 
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        uf = UnionFind(grid)
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    grid[i][j] == "0"
                    if i - 1 >= 0 and grid[i-1][j] == "1":
                        uf.union(nc*i + j, nc*(i-1) + j)
                    if i + 1 < nr and grid[i+1][j] == "1":
                        uf.union(nc*i + j, nc*(i+1) + j)
                    if j - 1 >= 0 and grid[i][j-1] == "1":
                        uf.union(nc*i + j, nc*i + j-1)
                    if j + 1 < nc and grid[i][j+1] == "1":
                        uf.union(nc*i + j, nc*i + j+1)


        return uf.get_count()


class UnionFind:
    def __init__(self, grid):
        self.count = 0
        m, n = len(grid), len(grid[0])
        self.parent = []
        self.rank = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    """
    Variant 4:
    The official solution provided by leetcode for the UnionFind approach. This is 
    essentially the same as Variant 3, with some optimizations. This is superior to
    Variant 3 in terms of RT efficiency, beating ~54% of accepted answers, but is the
    same in terms of memory efficiency, beating ~43% of accepted answers.
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        uf = UnionFind(grid)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    if r - 1 >= 0 and grid[r - 1][c] == "1":
                        uf.union(r * nc + c, (r - 1) * nc + c)
                    if r + 1 < nr and grid[r + 1][c] == "1":
                        uf.union(r * nc + c, (r + 1) * nc + c)
                    if c - 1 >= 0 and grid[r][c - 1] == "1":
                        uf.union(r * nc + c, r * nc + c - 1)
                    if c + 1 < nc and grid[r][c + 1] == "1":
                        uf.union(r * nc + c, r * nc + c + 1)

        return uf.getCount()

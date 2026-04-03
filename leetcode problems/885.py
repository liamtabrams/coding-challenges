"""
885. Spiral Matrix III
Attempted
Medium

Topics

Companies
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

 

Example 1:


Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:


Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
 

Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
"""

class Solution:
    """
    Variant 1:
    My first successful attempt at solving this leetcode problem. This particular solution
    beat only ~5% of accepted answers in terms of run time and ~35% of accepted answers in
    terms of memory efficiency. The run time complexity of this particular solution is
    O(n x m) and the memory complexity of this particular solution is also O(n x m), where
    n and m represent the number of rows and columns respectively. Leetcode wasn't able to
    analyze the time and space complexity of my submission because the 'submission length 
    exceeds limit', lol.
    """
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        rows = [i for i in range(rows)]
        cols = [j for j in range(cols)]
        visited = [[rStart, cStart]]
        currentR = rStart
        currentC = cStart
        direction = 'east'
        radius = 1

        while len(visited) < len(rows)*len(cols):
            if direction == 'east':
                if currentC - cStart < radius:
                    currentC += 1
                    if currentR in rows and currentC in cols and [currentR, currentC] not in visited:
                        visited.append([currentR, currentC])
                else:
                    direction = 'south'
                    currentR += 1
                    if currentR in rows and currentC in cols and [currentR, currentC] not in visited:
                        visited.append([currentR, currentC])
            elif direction == 'south':
                if currentR - rStart < radius:
                    currentR += 1
                    if currentR in rows and currentC in cols and [currentR, currentC] not in visited:
                        visited.append([currentR, currentC])
                else:
                    direction = 'west'
                    currentC -= 1
                    if currentR in rows and currentC in cols and [currentR, currentC] not in visited:
                        visited.append([currentR, currentC])
            elif direction == 'west':
                if cStart - currentC < radius:
                    currentC -= 1
                    if currentR in rows and currentC in cols and [currentR, currentC] not in visited:
                        visited.append([currentR, currentC])
                else:
                    direction = 'north'
                    currentR -= 1
                    if currentR in rows and currentC in cols and [currentR, currentC] not in visited:
                        visited.append([currentR, currentC])
            else:
                if rStart - currentR < radius:
                    currentR -= 1
                    if currentR in rows and currentC in cols and [currentR, currentC] not in visited:
                        visited.append([currentR, currentC])
                else:
                    direction = 'east'
                    currentC += 1
                    if currentR in rows and currentC in cols and [currentR, currentC] not in visited:
                        visited.append([currentR, currentC])
            if rStart - currentR == currentC - cStart == radius:
                radius += 1

        return visited


class Solution:
    """
    Variant 2:
    This is me reproducing 'Approach 1: Simulation' given by leetcode. This particular 
    solution beat ~65% of accepted answers in terms of run time and ~50% of accepted
    answers in terms of memory efficiency. The run time complexity of this particular 
    solution is O(n x m) and the memory complexity of this particular solution is also 
    O(n x m), where n and m represent the number of rows and columns respectively. 
    This time Leetcode WAS able to analyze the time and space complexity of my submission,
    and confirmed it is O(n x m) for both. However, the editorial section explains that the
    time complexity of this solution is actually O(max(n,m)^2), since that determines the
    total distance traversed along the path of the spiral. Why is this solution so much more
    efficient than Variant 1, in terms of both time and space? Well, all of the extra 
    comparison operations required to traverse the logic, as well as the unnecessary list 
    lookup "and [currentR, currentC] not in visited" before appending to visited, makes the 
    run time efficiency of Variant 1 quite poor. This solution circumvents all of that 
    logic and unnecessary list lookup using the facts that the number of steps in any given
    direction while following the spiral path is always the same for specific pairs of 
    directions (which are east & south and west & north) before increasing by 1 for the 
    following section, and that no previously traversed cell will be landed on again, by
    following the spiral path. The fact that I defined unnecessary additional variables 
    'currentR' and 'currentC' as well as unnecessary lists 'rows' and 'cols' in Variant 1
    explains why it is also less memory efficient than this solution.
    """
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        step = 1
        traversed = []
        direction = 0
        while len(traversed) < rows * cols:
            for _ in range(2):
                for j in range(step):
                    if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                        traversed.append([rStart, cStart])
                    rStart += movement[direction][0]
                    cStart += movement[direction][1]
                direction = (direction + 1)%4
            step += 1
    
        return traversed
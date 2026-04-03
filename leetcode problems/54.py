"""
54. Spiral Matrix
Solved
Medium
Topics
Companies
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    '''
    Variant 1:
    My first successful attempt at solving this problem. I don't think it is a particularly
    elegant way to solve this problem, and was teeming with bugs at first, but it is a
    straightforward approach and was relatively easy to debug. The run time complexity of
    this particular solution is O(m*n) where m and n are the number of rows and columns of
    'matrix' respectively, and the space complexity is O(m*n) as well, since we create two
    arrays, 'spiral_order' and 'included_cells', which each get filled with m*n elements.
    Unfortunately because the code is so long LC was not able to analyze the complexities 
    in order for me to confirm these claims, but I am pretty confident in them. This
    solution beats ~50% and 13% of accepted answers in terms of RT and memory efficiency
    respectively. These numbers sounds about right. This isn't necessarily computationally
    slow but is probably spatially inefficient/redundant. 
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        spiral_order = []
        curr = [0, 0]
        spiral_order.append(matrix[curr[0]][curr[1]])
        included_cells = [curr.copy()]
        print(included_cells)
        direction = 'east'
        while len(spiral_order) < m*n:
            print(included_cells)
            if direction == 'east':
                if curr[1] < n-1:
                    if [curr[0],curr[1]+1] not in included_cells:
                        spiral_order.append(matrix[curr[0]][curr[1]+1])
                        curr[1] += 1
                        included_cells.append(curr.copy())
                    else:
                        direction = 'south'
                        spiral_order.append(matrix[curr[0]+1][curr[1]])
                        curr[0] += 1
                        included_cells.append(curr.copy())
                        continue

                else:
                    direction = 'south'
                    spiral_order.append(matrix[curr[0]+1][curr[1]])
                    curr[0] += 1
                    included_cells.append(curr.copy())
                    continue
            if direction == 'south':
                if curr[0] < m-1:
                    '''print(curr[0])
                    print(curr[1])'''  
                    if [curr[0]+1,curr[1]] not in included_cells:
                        spiral_order.append(matrix[curr[0]+1][curr[1]])
                        curr[0] += 1
                        included_cells.append(curr.copy())
                    else:
                        direction = 'west'
                        spiral_order.append(matrix[curr[0]][curr[1]-1])
                        curr[1] -= 1
                        included_cells.append(curr.copy())
                        continue
                else:
                    direction = 'west'
                    spiral_order.append(matrix[curr[0]][curr[1]-1])
                    curr[1] -= 1
                    included_cells.append(curr.copy())
                    continue
            if direction == 'west':
                if curr[1] > 0: 
                    if [curr[0],curr[1]-1] not in included_cells:
                        spiral_order.append(matrix[curr[0]][curr[1]-1])
                        curr[1] -= 1
                        included_cells.append(curr.copy())
                    else:
                        direction = 'north'
                        spiral_order.append(matrix[curr[0]-1][curr[1]])
                        curr[0] -= 1
                        included_cells.append(curr.copy())
                        continue
                else:
                    direction = 'north'
                    spiral_order.append(matrix[curr[0]-1][curr[1]])
                    curr[0] -= 1
                    included_cells.append(curr.copy())
                    continue
            if direction == 'north':
                print(included_cells)
                if [curr[0]-1,curr[1]] not in included_cells:
                    spiral_order.append(matrix[curr[0]-1][curr[1]])
                    curr[0] -= 1
                    included_cells.append(curr.copy())
                else:
                    direction = 'east'
                    spiral_order.append(matrix[curr[0]][curr[1]+1])
                    curr[1] += 1
                    included_cells.append(curr.copy())
                    continue

        return spiral_order


class Solution:
    """
    Variant 2:
    My successful reproduction of 'Approach 1: Set Up Boundaries' given by LC. This
    solution has a run time time complexity of O(m*n) and a space complexity of O(1),
    since according to LC we don't use other data structures and we DO NOT include the
    output array in the space complexity. This solution beats ~50% and ~50% of accepted
    answers in terms of run time and memory efficiency respectively. 
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        up = 0
        left = 0
        down = rows - 1
        right = cols - 1
        spiral_order = []
        while len(spiral_order) < rows*cols:
            for col in range(left, right+1):
                spiral_order.append(matrix[up][col])

            for row in range(up+1, down+1):
                spiral_order.append(matrix[row][right])

            if up != down:
                for col in range(right-1, left - 1, -1):
                    spiral_order.append(matrix[down][col])

            if right != left:
                for row in range(down-1, up, -1):
                    spiral_order.append(matrix[row][left])

            up += 1
            down -= 1
            right -= 1
            left += 1

        return spiral_order   


class Solution:
    """
    Variant 3:
    The official solution for 'Approach 1: Set Up Boundaries' given by LC for this problem.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result


class Solution:
    """
    Variant 4:
    The official solution for 'Approach 2: Mark Visited Elements' given by LC for this
    problem. Like Approach 1, this solution has a time complexity of O(m*n) and a space
    complexity of O(1). This solution doesn't display a noticeable difference in
    performance from Variant 3, beating ~50% and ~50% of accepted solutions in terms of
    RT and memory efficiency, respectively.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right.
        current_direction = 0
        # The number of times we change the direction.
        change_direction = 0
        # Current place that we are at is (row, col).
        # row is the row index; col is the column index.
        row = col = 0
        # Store the first element and mark it as visited.
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:

            while True:
                # Calculate the next place that we will move to.
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds.
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell.
                if matrix[next_row][next_col] == VISITED:
                    break

                # Reset this to 0 since we did not break and change the direction.
                change_direction = 0
                # Update our current position to the next step.
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change our direction.
            current_direction = (current_direction + 1) % 4
            # Increment change_direction because we changed our direction.
            change_direction += 1

        return result


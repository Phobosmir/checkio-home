"""
Can You Pass?
 Simple
English DE ES RU
If you have solved the "How to find friends" mission, then you already know how to check for the existence of a path in graphs. Let's try to add something more to that problem.

You are given a matrix (2D array) and the coordinates (row and column) of two cells with the same value. The matrix consists of digits.
You may move to neighbouring cells either horizontally or vertically provided the values of the origin and destination cells are equal.
You should determine if a path exists between two given cells.

A matrix is represented as a tuple of tuples with digits.
Coordinates are represented as a tuple with two numbers: row and column.
The result should be any value which can be converted into a boolean.
If a path exists, then return True. Return False if there is none.

can-you-jump-through

Input: Three arguments. A matrix as a tuple of tuples with integers, first and second cell coordinates as tuples of two integers.

Output: The existence of a path between two given cells as a boolean or a value that can be converted to boolean.

Example:
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 2), (0, 5)) == True, 'First example'
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 3), (6, 0)) == False,

How it is used: Sometimes we don't need the full pathfinding algorithms implementation and can use simplified realisation of these algorithms. It can be an useful skill to find a simple ways.

Precondition:
1 < len(matrix) ≤ 10
all(1 < len(row) ≤ 10 for row in matrix)
all(all(0 ≤ x < 10 for x in row) for row in matrix)
matrix[first[0]][first[1]] == matrix[second[0]][second[1]]
first != second
"""

"""
from itertools import product
from math import hypot


def can_pass(matrix, start, end):
    reachable = set([start])
    cells = product(range(len(matrix)), range(len(matrix[0])))
    valid_cells = {(x, y) for x, y in cells if matrix[x][y] == matrix[start[0]][start[1]]}
    while True:
        neighbours = set((x, y) for x, y in valid_cells if any(hypot(x-a, y-b) == 1 for a, b in reachable))
        if end in neighbours:
            return True
        if not neighbours:
            return False
        reachable |= neighbours
        valid_cells -= reachable
"""



def can_pass(matrix, first, second):
    rows, cols = get_matrix_dimensions(matrix)
    start_val = matrix[first[0]][first[1]]
    if start_val != matrix[second[0]][second[1]]:
        raise ValueError('Initial and dest point values are not equal!')

    points_to_visit = [first]
    visited = set()
    while points_to_visit:
        cur_point = points_to_visit.pop()
        neighbors = get_neighbor_indexes(cur_point, rows, cols)
        for point in neighbors:
            if point == second:
                return True
            if point in visited:
                continue

            if matrix[point[0]][point[1]] != start_val:
                continue

            if point not in points_to_visit:
                points_to_visit.append(point)

        visited.add(cur_point)
    return False


def get_matrix_dimensions(matrix):
    rows = len(matrix)
    if rows == 0:
        raise ValueError('Matrix has no rows')
    cols = len(min(matrix))
    if cols == 0:
        raise ValueError('Matrix has an empty row, w/o columns')
    return rows, cols


def get_neighbor_indexes(point, rows, cols):
    x, y = point
    near_points = [(x, y) for x, y in ((x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y))]
    return filter(lambda point: 0 <= point[0] < rows and 0 <= point[1] < cols, near_points)

if __name__ == '__main__':
    # assert can_pass(((0, 0, 0, 0, 0, 0),
    #                  (0, 2, 2, 2, 3, 2),
    #                  (0, 2, 0, 0, 0, 2),
    #                  (0, 2, 0, 2, 0, 2),
    #                  (0, 2, 2, 2, 0, 2),
    #                  (0, 0, 0, 0, 0, 2),
    #                  (2, 2, 2, 2, 2, 2),),
    #                 (3, 2), (0, 5)) == True, 'First example'
    # assert can_pass(((0, 0, 0, 0, 0, 0),
    #                  (0, 2, 2, 2, 3, 2),
    #                  (0, 2, 0, 0, 0, 2),
    #                  (0, 2, 0, 2, 0, 2),
    #                  (0, 2, 2, 2, 0, 2),
    #                  (0, 0, 0, 0, 0, 2),
    #                  (2, 2, 2, 2, 2, 2),),
    #                 (3, 3), (6, 0)) == False, 'First example'

    # assert can_pass(((5, 6),
    #                 (6, 6),
    #                  (6, 5),
    #                  (6, 6),
    #                  (7, 6),
    #                  (6, 6),
    #                  (6, 7),
    #                  (6, 6),
    #                  (8, 6),
    #                  (6, 6)),
    #
    #                 (9, 1),
    #                 (0, 1)) == True

    assert can_pass(((3,3,2,2,2),(2,2,3,3,3),(3,3,2,2,2),(3,2,2,2,3),(2,3,2,2,2),(2,3,2,3,3)), (5,2), (0,2)) == False



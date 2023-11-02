#!/usr/bin/python3
"""
a Python program that solves the N queens problem
using a backtracking algorithm
"""
import sys


solutions = []
"""store the list of possible solutions.
"""
n = 0
"""The size of the chessboard.
"""
pos = None
"""a list that holds all possible positions on the chessboard.
"""


def get_input():
    """
    retrieves and validates the user-provided argument,
    which is the size of the chessboard (N).
    checks
    :if the argument count is correct
    :if N is a valid integer
    :if N is at least 4
    :if error: exits the program with a status code of 1.
    """
    global n
    n = 0
    """Check the number of command-line arguments
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """
    checks whether two queens in given positions are in
    an attacking position. It considers both row and column
    conflicts as well as diagonal conflicts.
    Args:
        pos0 (list or tuple): 1st queen's position.
        pos1 (list or tuple): 2ndqueen's position.
    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """
    checks if a group of positions (a possible solution) already exists
    in the list of solutions. It compares each position in the group to
    the positions in existing solutions. If a matching group is found,
    it returns True.
    Args:
        group (list of integers): A group of possible positions.
    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """
    a recursive backtracking function that builds valid solutions
    for the N queens problem.
    If the row reaches n, it means a solution is found and adds it to
    the solutions list if it doesn't already exist.
    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """
    initializes the pos list with all possible positions on the chessboard
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)

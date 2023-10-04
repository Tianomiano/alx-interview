#!/usr/bin/python3
"""
n number of locked boxes.
the boxes are numbered sequentially from 0 to n - 1
each box contains keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    determine if all the boxes can be opened.
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False

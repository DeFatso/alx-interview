#!/usr/bin/python3
def canUnlockAll(boxes):
    """
        Return True if all boxes can be opened, else return False
    """
    n = len(boxes)
    if n == 0:
        return True

    opened = [False] * n
    opened[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)

#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    # Set to keep track of opened boxes
    opened_boxes = set()

    # Initialize a queue with the first box
    queue = [0]

    # Perform BFS
    while queue:
        current_box = queue.pop(0)
        opened_boxes.add(current_box)

        # Add keys from the current box to the queue
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                queue.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)

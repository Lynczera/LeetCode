from typing import List

"""
two pointer, 1 at the beginning, 1 at the end. Move pointers towards each other and 
calculates the curr max. we can always move the pointer that has the lowest height.
 
"""


def maxArea(height: List) -> int:
    i = 0
    j = len(height) - 1
    curr_max_area = 0
    while i < j:
        curr = ((j - i)) * min(height[i], height[j])
        if curr > curr_max_area:
            curr_max_area = curr

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return curr_max_area

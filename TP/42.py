from typing import List

"""
one pointer at the beginning, one at the end. For each block, 
the amount of water will be -> min(l,r) - block[i]
where l = max of left, r = max of right 
we check the curr block we are in. How to now which block?

we always move the min(l,r). The next value of the increment will be the curr block we 
will look at. after doing the math, we can update l or r accordingly. 

lets say min of l,r is l. This means that we will have at least one block on the right that,
combine with this l, will create a trap. 
"""


def trap(height: List) -> int:
    i = 0
    j = len(height) - 1
    maxL = height[i]
    maxR = height[j]
    result = 0
    while j > i:
        if maxL < maxR:
            i += 1
            curr = min(maxL, maxR) - height[i]
            if curr > 0:
                result += curr
            if height[i] > maxL:
                maxL = height[i]

        else:
            j -= 1
            curr = min(maxL, maxR) - height[j]
            if curr > 0:
                result += curr
            if height[j] > maxR:
                maxR = height[j]

    return result

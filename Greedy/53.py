from typing import List

"""
We can use a dp approach.

the subcases are subarrays where the curr possible max subarray ends at the specific index.
however, as we calculate the possible solutions, we can either continue the previous sequence, or 
start a new one. 
"""


def maxSubArray(self, nums: List[int]) -> int:

    curr = nums[0]
    max_sum = curr
    for i in range(1, len(nums)):
        if curr + nums[i] > nums[i]:
            curr += nums[i]
        else:
            curr = nums[i]
        if curr > max_sum:
            max_sum = curr

    return max_sum


def simplified(self, nums: List[int]) -> int:
    curr = nums[0]
    max_sum = curr

    for i in range(1, len(nums)):
        curr = nums[i] + max(0, curr)
        if curr > max_sum:
            max_sum = curr
    return max_sum

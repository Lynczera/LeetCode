'''
put items in hashmap
once the item we adding is already contained in the hashmap, return true
if we add everything without returning true, we return false
'''

from ast import List


def containsDuplicate(nums: List[int]) -> bool:
    count = dict()
    for num in nums:
        if num in count:
            return True
        else:
            count[num] = 1
    
    return False


'''
Turn array into a set

for each element in the set:
first we track the max sequence

if element-1 not in set, this is the start of a sequence.
while element +1 in set, keep counting. if element +1 not in set, we are done
with this current sequence.

we do this and keep track of max sum so far

'''

def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    result = 0

    for num in nums_set:
        if num-1 not in nums_set:
           #start of seq
            curr_max=0
            curr = num 

            while curr in nums_set:
                curr_max +=1
                curr = curr+1
            result = max(result, curr_max) 
    return result
              

'''
have a dict to map each num and its index
as we loop over nums and add them to the dict, we check if target - num is in the dict 

if its not, we just add that object to dict

this approach works because the result needs to be a pair. 

'''

def twoSum(nums: List[int], target: int) -> List[int]:
    freq = dict()
    
    for i in range(len(nums)):
        if target - nums[i] in freq:
            result = []
            result.append(i)
            result.append(freq[target - nums[i]])
            return result
        else:
            freq[nums[i]] = i
        
    return []


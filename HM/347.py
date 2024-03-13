'''
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

create a dict that tracks the frequency of each number 
{1:3, 2:2, 3:1} 

then, we can create an array with the frequencies matching the indexes 
[0, 3, 2, 1]
'''

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = dict()
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    buckets = [[]]*(max(list(freq.values()))+1)

    for key, value in freq.items():
        buckets[value] = buckets[value] + [key]

    result = []
    i = 0

    for j in range(len(buckets)-1, 0, -1):
        if len(buckets[j]) > 0 and i<k:
            for num in buckets[j]:
                if i<k:
                    result.append(buckets[j])
                    i+=1
    return result


    




    








    
    
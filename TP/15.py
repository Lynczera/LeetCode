'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]


turn in to a two pointer problem:
    fix one value and use two pointer approach-> for each num in nums, 2 tp approach = n^2?


Solution:
Sort
fix 1 element at a time. 
do multiple two sum 2 problems 

create 2 sets. First tracking duplicates with the 1st element. Second to track duplicates with the 2nd element

'''

#  Input: nums = [-1,0,1,2,-1,-4]
def threeSum(nums) :
    nums = sorted(nums)
    result = []
    seen = set()
    
    for i,val in enumerate(nums):
        j = i+1 
        k = len(nums)-1
        track = dict()
        seen2 = set()
        
        if val in seen:
            continue
        else: seen.add(val)

        while j < k:
            if val + nums[j] + nums[k] == 0: 
                if nums[j] not in seen2:
                    result.append([val, nums[k], nums[j]])
                    seen2.add(nums[j])
                    k-=1
                    j+=1
                    
                else:
                    j+=1
            else:
                if val + nums[j] + nums[k] > 0: k-=1
                if val + nums[j] + nums[k] < 0: j+=1


    return result                 







        
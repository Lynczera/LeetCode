'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

first solution -> prefix and postfix array
//calculating prefix
pre = [1, 2*1, 3*2*1, 4*3*2*1]
//calculating postfix
pos = [1*2*3*4,2*3*4,3*4,4]

ans = [2*3*4, 1*3*4, 2*1*4, 3*2*1]
'''
def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = [1]*len(nums)
    postfix = [1]*len(nums)
    prefix[0] = nums[0]
    postfix[-1] = nums[-1]

    #calculate prefix 
    for i in range(1,len(nums)):
        prefix[i] = nums[i]*prefix[i-1]

    #calculate postfix
    for i in range(len(nums)-2, 0,-1):
        postfix[i] = nums[i]*postfix[i+1]

    answer = [1]*len(nums)
    answer[0] = postfix[1]

    answer[-1]= prefix[len(nums)-2]

    for i in range(1,len(nums)-1):
        answer[i] = prefix[i-1] * postfix[i+1]
    
    return answer


'''
opt solution -> prefix and postfix carrying each ...fix

prefix = 1->2->6->4
ans = [1,1,2,6]

postfix = 24
ans = [24,12,8,6]

Here, we set multiple the answer at index by the prefix and then
we update the prefix 

we do the same thing for postfix 

remember that the first item only need postfixes 
and last item only need prefixes 

Therefore, once you first calculate the prefixes, the last item is already
the answer, and the first item is not unchanged. So, when you calculate the 
post fix, the first item will be updated accordingly.
'''
def opt_productExceptSelf(nums: List[int]) -> List[int]:
    answer = [1]*len(nums)
    prefix = nums[0]

    for i in range(1, len(nums)):
        answer[i]*=prefix
        prefix*=nums[i]
    
    postfix = nums[-1]

    for i in range(len(nums)-2, -1, -1):
        answer[i]*=postfix
        postfix*=nums[i]
    
    return answer

    
    


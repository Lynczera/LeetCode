def search(nums: List[int], target: int) -> int:

    i = 0
    j = len(nums)-1

    while i <= j:
        mid = math.floor((i+j)/2)
        
        if(nums[mid] == target): return mid
        
        if nums[mid] < target:
            i = mid+1
        if nums[mid] > target:
            j = mid-1

    return -1
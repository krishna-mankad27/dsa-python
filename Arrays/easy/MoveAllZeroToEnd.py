def MoveZeroToEnd(nums):
    n = len(nums)
    i = 0
    j = 0
    while j < n:
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            
            i+=1
        j+=1
    return nums

print(MoveZeroToEnd([4,0,6,8,0,1,0,9,0,4]))
def LeftRotateByOne(nums):
    temp = nums[0]
    for i in range(1,len(nums)):
        nums[i-1],nums[i]=nums[i],nums[i-1]
    nums[-1]= temp
    return nums
#return LeftRotateByOne(nums)
print(LeftRotateByOne([1,2,3,5,6]))
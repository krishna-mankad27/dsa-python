def RecursiveInsertionSort(nums,i):
    if i>len(nums)-1:
        return nums
    a = i
    while i > 0 and nums[i]<nums[i-1]:
        nums[i],nums[i-1]=nums[i-1],nums[i]
        i-=1
    RecursiveInsertionSort(nums,a+1)
    return nums

print(RecursiveInsertionSort([1,3,8,5,4,2,9,7],1))


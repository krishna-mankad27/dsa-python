def RecursiveBubbleSort(nums,n):
    flag = 0
    i = 0
    if n <1:
        return nums
    while i<n-1:
        if nums[i] > nums[i+1]: 
            nums[i],nums[i+1]=nums[i+1],nums[i]
            flag +=1
        i+=1
    if flag == 0:return nums
    RecursiveBubbleSort(nums,n-1)
    return nums

a = [1,2,3,4,5,6,7,8]
print(RecursiveBubbleSort(a,len(a)))









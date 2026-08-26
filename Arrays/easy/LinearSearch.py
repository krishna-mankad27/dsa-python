def LinearSearch(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i 
    return -1

print(LinearSearch([1,2,5,8,9,6,3,4],78))
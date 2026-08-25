def LargestElement(nums):
    lar = nums[0]
    for i in range(len(nums)):
        if nums[i]>lar:
            lar = nums[i]
    return lar

print(LargestElement([1,5,3,9,2,78,1,56,59,59]))
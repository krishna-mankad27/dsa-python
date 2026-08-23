def InsertionSort(nums):
    for i in range(1,len(nums)):
        j = i-1
        while nums[j+1]<nums[j] and j>=0:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            j -=1
    return nums

a = [1,5,3,9,2,4,6]
print(InsertionSort(a))
            
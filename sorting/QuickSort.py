def QuickSort(nums,low,high):
    if low<high:
        pivot = partition(nums,low,high)
        QuickSort(nums,low,pivot-1)
        QuickSort(nums,pivot+1,high)
    return nums

def partition(nums,low,high):
    pivot = nums[low]
    i = low
    j = high
    while i<j:
        while nums[i]<=pivot and i<high:
            i+=1
        while nums[j]>pivot and j>low:
            j-=1
        if i< j:nums[i],nums[j]=nums[j],nums[i]
        nums[low],nums[j]=nums[j],nums[low]
    return j

a = [4,6,2,1,7,5,9,8]
print(QuickSort(a,0,len(a)-1))
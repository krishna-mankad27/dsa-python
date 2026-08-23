def MergeSort(nums,low,high):
    #base case
    if low >=high:
        return
    mid = int((low+high)/2)
    MergeSort(nums,low,mid)
    MergeSort(nums,mid+1,high)
    Merge(nums,low,mid,high)
    return nums

def Merge(nums,low,mid,high):
    temp = []
    left = low
    right = mid+1
    while left<=mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
    while left<=mid:
        temp.append(nums[left])
        left+=1
    while right<=high:
        temp.append(nums[right])
        right+=1
    for i in range(low,high+1):
        nums[i] = temp[i-low]

a = [3,9,4,5,1,8,2,7]
print(MergeSort(a,0,len(a)-1))
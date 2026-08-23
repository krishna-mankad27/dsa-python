def BubbleSort(nums):
    for i in range(0,len(nums)-1):
        ifswap = 0                                  #for alreaady sorted list 
        for j in range(0,len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                ifswap +=1
        if ifswap == 0:                             #checking for alreaady sorted list
            break
    return nums
a = [1,2,32,56,87]
print(BubbleSort(a))
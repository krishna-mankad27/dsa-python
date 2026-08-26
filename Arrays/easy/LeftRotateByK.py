def LeftRotateByK(nums,k):
    n = len(nums)
    k = k%n
    if (k == 0):return nums
    temp = [0]*k
    for j in range(k):
        temp[j] = nums[j]
    for i in range(k,n):
        nums[i-k] = nums[i]
    for l in range(k,0,-1):
        nums[n-l] = temp[-l]
    
    return nums
#return LeftRotateByK(nums)
print(LeftRotateByK( [3, 4, 1, 5, 3, -5],8))

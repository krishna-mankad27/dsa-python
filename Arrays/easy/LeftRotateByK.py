def LeftRotateByK(nums,k):
    
    n = len(nums)          #--optimised approach
    k = n- k%n                                             
    nums[0:k]=nums[0:k][::-1]
    nums[k:n]=nums[k:n][::-1]
    nums=nums[::-1]

    # n = len(nums)        ---brute force approach
    # k = k%n
    # if (k == 0):return nums
    # temp = nums[0:k]
    # for i in range(k,n):
    #     nums[i-k] = nums[i]
    # for l in range(k,0,-1):
    #     nums[n-l] = temp[-l]
    
    return nums
#return LeftRotateByK(nums)
print(LeftRotateByK([1,2,3,4,5,6,7],3))

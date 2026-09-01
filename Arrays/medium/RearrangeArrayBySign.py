def RearrangeBySign(nums):
    n = len(nums)
    #brute solution-> make 2 arrays for both signs put each signed in their array then 
                    # reiterate through main array and put positive in even index and negative in odd index
                    #  tc-> O(n) + O(n/2) Sc -> O(N)
    # pos = []
    # neg = []
    # for i in range(n):
    #     if nums[i] < 0:neg.append(nums[i])
    #     else: pos.append(nums[i])
    # for i in range(n):
    #     nums[2*i] = pos[i]
    #     nums[2*i+1] = neg[i]
#-------------------------------------------------------------------------------------------------------
    #optimal solution ->
    pos = 0
    neg = 1
    i = 0
    while i < n and pos<n:
        if nums[i] %2 == 0:
            nums[i] , nums[pos] = nums[pos],nums[i] 
            pos +=2
        else:i+=1

        
    return nums
print(RearrangeBySign([2, 4, 5, -1, -3, -4]))
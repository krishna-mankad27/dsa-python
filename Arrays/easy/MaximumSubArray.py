def MaxSubArray(nums):
    n = len(nums)
    #Brute force solution -> tc O(N^3), sc ->O(1)
    maxtotal = 0
    for i in range(n):
        for j in range(i,n):
            total = 0
            for k in range(i,j+1):
                total += nums[k]
                maxtotal = max(total,maxtotal)
    #better solution ->tc O(N^2), sc -> O(1)
    for i in range(n):
        total = 0
        for j in range(i,n):
            total += nums[k]
            maxtotal = max(total,maxtotal)
    #optimal solution "Kadaane's algo" -> iterate through all numbers keep adding till
                                        # sum > 0 if sum<0 sum = 0 then keep iterating and adding
    maxtotal = float("-inf")
    total = 0
    for i in range(n):
        total += nums[i]
        if maxtotal< total:
            maxtotal = total
        if total<0:
            total = 0


    return maxtotal
print(MaxSubArray( [-3, -3, -7, -2, -1, -4]))
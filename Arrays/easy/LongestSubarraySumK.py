def LongestSubarraySumK(nums,k):
    n = len(nums)
    #Brute Solution -> generate all subarray 
    maxlen1 = 0
    for i in range(n):
        total = 0
        for j in range(i,n):
            total += nums[j]
            if total == k :
                maxlen1 = max(maxlen1,j+1-i)
#------------------------------------------------------ 
    #better solution -> using hashmap to save sum of subarrays and find new subarrays with sum k
    preSumMap= {}
    total = 0
    maxlen2 = 0
    for i in range(n):
        total += nums[i]
        if total == k:
            maxlen2 = max(maxlen2,i+1)
        rem = total - k
        if rem in preSumMap :
            length = i - preSumMap[rem]
            maxlen2 = max(maxlen2,length)
        if total not in preSumMap:
            preSumMap[total] = i
#-----------------------------------------------------
    #optimal solution (only for positive numbers) -> 2 pointer 
    maxlen3 = 0
    i = 0
    total = 0
    for j in range(n):
        total +=nums[j]
        while total>k:
                    total -=nums[i]
                    i+=1
        if total == k :
            maxlen3 = max(maxlen3,j-i+1)
            
    return maxlen1,maxlen2,maxlen3 
    
    
print(LongestSubarraySumK([1,2,3,1,1,1,1,4,3,2],3))




def TwoSum(nums,k):
    n=len(nums)
    #Brute Solution -> double nested for loop
    # for i in range(n):
    #   for j in range(i+1,n):
    #         if nums[i] + nums[j]==k:
    #             return True
#----------------------------------------------------------
    #Better solution -> using hashmap/dict store all element first then
                        #check one by one if remainder is available in arrya already from hashmap
    data = {}
    for i in range(n):
        rem = k - nums[i]
        if rem in data:
            return True , [data[rem][1],i]
        data[nums[i]] = [1,i]
#---------------------------------------------------------------------------------------------------------
    #optimal solution -> use two pointers one at start and second at end then increase first if 
                        #sum smaller then target else decrease end pointer
    i = 0
    j = n-1
    nums.sort()
    while i < j:
        if nums[i]+nums[j] == k:
            return True , [i,j]," After Sorting"
        elif nums[i]+nums[j] < k:
            i+=1
        else:
            j-=1

    
    return False


print(TwoSum([1,1,1,5,8,2,6,9,8,2],17))

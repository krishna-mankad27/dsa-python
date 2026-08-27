def FindNumberAppearingOnce(nums):
    n = len(nums)
    #Brute force solution
    # for i in range(n):
    #     count = 0
    #     for j in range(n):
    #         if nums[i] == nums[j]:
    #             count+=1
    #     if count == 1:
    #         return nums[i]
#------------------------------------------
    #better solution ->Using hashing
    # my_dict = {}
    # for i in range(n):
    #     my_dict[nums[i]] = 0
    # for i in range(n):
    #     my_dict[nums[i]] += 1
    # for i in range(n):
    #     if my_dict[nums[i]] == 1:
    #         return nums[i]
#------------------------------------------
    #optimal solution ->Using XOR since n^n = 0 
    xor = 0
    for i in range(n):
        xor = xor^nums[i]
    return xor

print(FindNumberAppearingOnce([1,1,3,3,5,6,4,4,5,8,8,9,9,6,7]))
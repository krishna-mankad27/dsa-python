def MissingNumber(nums):
    n = len(nums) +1
    #most opitmal using xor operation
    xor1 = 0
    xor2 = 0
    for i in range(n-1):
        xor1 = xor1^nums[i]
        xor2 = xor2^(i+1)
    xor2 = xor2^(n)
    #return xor1^xor2
#-----------------------------------------------
    #optimal using sum of first N numbers
    total = 0
    for i in range(n-1):
        total +=nums[i]
    #return int((n)*(n+1)/2) - total
#-----------------------------------------------
    #better approach then brute force using hashmap 
    my_dict = dict.fromkeys(range(n+1),0)
    for i in range(n-1):
        my_dict[nums[i]] =1
    for i in range(1,n+1):
        if my_dict[i] == 0:
            return i 
#-----------------------------------------------
    #brute force method initate array with 1-N numbers then check for each if it exists in n via 2 nested for loops
            


print(MissingNumber([1,8,5,3,2,6,9,7]))


def MajorityElement(nums):
    count = 0
    #optimal solution -> moore's voting algorithm 
    for i in range(len(nums)):
        if count == 0:
            element = nums[i]
            count +=1
        elif nums[i] == element:
            count +=1
        else: count-=1
    count = 0
    for i in range(len(nums)):
        if nums[i] == element:
            count += 1
    if count>int(len(nums)/2):
        return element
    else:return None
    #brute ->count each elements total count using nested looping
    #better use a hashmap to count each element 

print(MajorityElement([1,2,2,1,1,1,0,0,0,0,0,0,0,0,2,1,1,]))
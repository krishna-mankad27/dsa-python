def SecondLargest(nums):
    lar = nums[0]
    check = 0
    lar2 = float('-inf')
    for i in range(len(nums)):
        if nums[i] > lar:
            lar2 = lar
            check +=1
            lar = nums[i]
        elif nums[i]>lar2 and nums[i]!= lar:
            lar2 = nums[i]
            check +=1
    if check == 0:return -1
    return lar2

print(SecondLargest([1,5,3,9,2,78,1,56,59,59]))

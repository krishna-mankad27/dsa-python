def SortZeroOneTwoOnlyArray(nums):
    n=len(nums)
    #optimal approach -> array ko (0,0,0,0|1,1,1,1|(0,1,2...)|2,2,2,2) me split kree basically 
                        #tc -> O(N) sc->O(1) {modifying given array}
    low,high,mid = 0,n-1,0
    while mid <=high:
        if nums[mid] == 0 :
            nums[mid],nums[low] = nums[low],nums[mid]
            low+=1
            mid+=1
        elif nums[mid] == 2:
            nums[mid],nums[high] = nums[high],nums[mid]
            high-=1
        else:
            mid+=1
    #brute -> sort array tc -> O(nlogn) sc -> O(1) or O(N){sorting}
    #better -> count in 1 pass then assign in 2nd pass -> tc -> O(2N) sc-> O(1) {modifying given array}
    return nums
print(SortZeroOneTwoOnlyArray([1,2,0,2,1,0,0,2,2,1,2]))

        
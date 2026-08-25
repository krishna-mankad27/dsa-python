def CheckIfSorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

a = [1,5,9,3,7]
b = [1,3,4,98,425,898]
print(CheckIfSorted(a),",",CheckIfSorted(b))
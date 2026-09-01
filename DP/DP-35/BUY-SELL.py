def BuyAndSell(nums):
    n = len(nums)
    minimum = nums[0]
    profit = 0
    for i in range(n):
        cost = nums[i] - minimum
        profit = max(profit,cost)
        minimum = min(nums[i],minimum)
    return profit

print(BuyAndSell([10, 7, 5, 8, 11, 9]))
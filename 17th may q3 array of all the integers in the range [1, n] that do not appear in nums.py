nums = [4,3,2,7,8,2,3,1]
n = len(nums)
result=[i for i in range(1, n+1)if i not in nums]
print(result)
nums = [4, 2, 5, 4]
val = 2
count = nums.count(val)
nums[:] = [num for num in nums if num != val]
nums += ['_'] * count
k = len(nums)
print("Output:", k, ", nums=", nums)

nums = [-1, 2, 1, -4]
target = 1
closest_sum = sum(nums[:3])
for i in range(len(nums) - 2):
    left, right = i + 1, len(nums) - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        closest_sum = min(closest_sum, total, key=lambda x: abs(x - target))
        left += total < target
        right -= total > target
print(closest_sum)

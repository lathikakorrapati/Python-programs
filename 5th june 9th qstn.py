nums = [5, 7, 7, 8, 8, 10]
target = 8
first_occurrence = -1
last_occurrence = -1
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
if left < len(nums) and nums[left] == target:
    first_occurrence = left
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] <= target:
        left = mid + 1
    else:
        right = mid - 1
if right >= 0 and nums[right] == target:
    last_occurrence = right
print([first_occurrence, last_occurrence])



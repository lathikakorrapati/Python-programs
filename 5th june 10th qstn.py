nums = [5,7,7,8,8,10]
target = 6
start = next((i for i, num in enumerate(nums) if num == target), -1)
end = next((i for i, num in enumerate(nums[::-1]) if num == target), -1)
if start != -1:
    end = len(nums) - 1 - end
print([start, end])

nums = [2, 7, 11, 15]
target = 9
Indices = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in Indices:
        print("Output:", [Indices[complement], i])
        break
    Indices[num] = i
nums = [-1, 0, 1, 2, -1, -4]
triplets = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                triplet = [nums[i], nums[j], nums[k]]
                triplet.sort()
                if triplet not in triplets:
                    triplets.append(triplet)
print(triplets)

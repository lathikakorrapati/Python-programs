nums2 = [1, 2]
distinct_nums = list(set(nums2))
distinct_nums.sort(reverse=True)
if len(distinct_nums) >= 3:
    result = distinct_nums[2]
 else:
     result = distinct_nums[0]

print(result)
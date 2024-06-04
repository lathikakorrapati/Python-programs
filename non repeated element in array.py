nums = [2, 2, 1, 4, 1]
single_number = 0
for num in nums:
    single_number ^= num

print("Output:",single_number)
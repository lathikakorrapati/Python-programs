nums=[2,2,3,3,5,5,5,4,7,7,7,7,8]
element_counts = {}
for num in nums:
    if num in element_counts:
        element_counts[num] += 1
    else:
        element_counts[num] = 1
print("Occurrences of each element in the list:")
for element, count in element_counts.items():
    print(element,'->',count)

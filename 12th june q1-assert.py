numbers = [1, 2, 3, -4, 5]
for num in numbers:
    assert num > 0, f"Found a non-positive integer: {num}"
print("All numbers are positive integers.")

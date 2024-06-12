numbers = [10, 20, 'a', 40, 50]
try:
    divisor = float(input("Enter a divisor: "))
    for num in numbers:
        print(f"{num} divided by {divisor} is {num / divisor}")
except ZeroDivisionError:
    print("Error: The divisor cannot be zero.")
except ValueError:
    print("Error: The divisor must be a numeric value.")
except TypeError as e:
    print(f"Error: {e}")

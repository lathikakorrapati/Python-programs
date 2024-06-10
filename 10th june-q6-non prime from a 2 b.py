A = 12
B = 19
for num in range(A, B+1):
 if num > 1:
     for i in range(2, num):
            if num % i == 0:
                print(num, end=", ")
                break

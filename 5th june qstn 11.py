num1 = "2"
num2 = "3"
if num1 == "0" or num2 == "0":
    print("0")
else:
    m, n = len(num1), len(num2)
    result = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        carry = 0
        for j in range(n - 1, -1, -1):
            temp = int(num1[i]) * int(num2[j]) + carry + result[i + j + 1]
            result[i + j + 1] = temp % 10
            carry = temp // 10
        result[i] += carry

    result_str = "".join(map(str, result))
    print(result_str.lstrip("0") if result_str != "0" else "0")

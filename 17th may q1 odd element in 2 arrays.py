s = ""
t = "y"
result = 0
for char in s:
    result ^= ord(char)
for char in t:
    result ^= ord(char)
added_character = chr(result)
print(added_character)

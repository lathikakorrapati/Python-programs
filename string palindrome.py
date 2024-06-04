s = input("Enter a string: ").lower()
s = (''.join(char for char in s if char.isalnum()))
left=0
right=len(s)-1
while left < right:
    if s[left] != s[right]:
        print("false")
        break
    left = left+1
    right = right-1
else:
    print("true")

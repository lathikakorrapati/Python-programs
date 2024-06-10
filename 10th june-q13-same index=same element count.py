str1="abcd"
str2="abcdef"
min_size=min(len(str1),len(str2))
count=0
for i in range(min_size):
    if str1[i] == str2[i]:
        count+=1
print("the number of same elements in same index in two strings is",count)
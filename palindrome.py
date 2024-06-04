num =int(input("enter a number:"))
temp=num
reverse=0
while(temp>0):
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp//10
if(num==reverse):
  print('Is a Palindrome')
else:
  print("Is not a Palindrome")
start=1
end=100
perfect_square=[]
num=1
while num*num<=end:
    square=num*num
    if square >= start:
        perfect_square.append(square)
    num+=1
print("list of numbers in the range that are perfect square are:",perfect_square)

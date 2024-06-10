x=4
y=5
result = x ^ y
hammingweight=0
while result:
    if result & 1:
        hammingweight+= 1
        result>>= 1
        print(hammingweight)

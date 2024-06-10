str="venkiteela is a very bad boy"
words=str.split()
count=0
for word in words:
    if word.startswith('V') or word.startswith('v'):
        count+=1
print(count)
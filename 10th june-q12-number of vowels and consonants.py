input_string = "koushik"
vowels_count=0
consonants_count=0
vowels=set("aeiouAEIOU")
for char in input_string:
    if char in vowels:
        vowels_count+=1
else: char.isalpha()
consonants_count+=1
print("vowels_count:",vowels_count)
print("consonants_count",consonants_count)

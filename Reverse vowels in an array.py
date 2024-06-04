s = "hello"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
vowel_indices = [i for i, char in enumerate(s) if char in vowels]
reversed_vowels = [s[i] for i in reversed(vowel_indices)]
for i, index in enumerate(vowel_indices):
    s = s[:index] + reversed_vowels[i] + s[index + 1:]
print("Reversed vowels string:", s)


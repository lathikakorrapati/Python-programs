def is_palindrome(sentence):
    normalized_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    return normalized_sentence == normalized_sentence[::-1]
sentence = "A man, a plan, a canal, Panama!"
if is_palindrome(sentence):
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")
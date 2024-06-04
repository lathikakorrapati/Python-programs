def longestCommonPrefix(strs):
    if not strs:
        return ""
    min_str = min(strs, key=len)
    prefix = ""
    for i, char in enumerate(min_str):
        if all(word[i] == char for word in strs):
            prefix = prefix + char
        else:
            break
    return prefix
strs1 = ["flower", "flow", "flight"]
print("Output:", longestCommonPrefix(strs1))

strs2 = ["camel", "cat", "car"]
print("Output:", longestCommonPrefix(strs2))
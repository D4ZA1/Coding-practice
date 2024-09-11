# given 2 strings, return true if the first string is a subsequence of the second string

def is_subsequence(str1, str2):
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
        j += 1
    return i == len(str1)

print(is_subsequence('abc','ahbgdc')) # True
print(is_subsequence('axc', 'ahbgdc')) # False

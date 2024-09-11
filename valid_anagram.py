#given 2 strings s and t, reutnr true if t is an anagram of s without sorting

def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    hashmap = {}
    for char in s:
        if char not in hashmap:
            hashmap[char] = 1
        else:
            hashmap[char] += 1
    for char in t:
        if char not in hashmap:
            return False
        else:
            hashmap[char] -= 1
    for key in hashmap:
        if hashmap[key] > 0:
            return False
    return True



    

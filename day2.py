"""
205. Isomorphic strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""
def isIsomorphic(s, t):
    # t.length == s.length
    dic = {}
    for x, y in zip(s, t):
        if x not in dic.keys() and y not in dic.values():
            dic[x] = y
        else:
            try:
                if dic[x] != y:
                    return False
            except KeyError:
                return False
    return True

# Lol, would never have put that together
# OHHHH, thats sneaky. So it gets all unique chars with set and then checks if the lens are equivalent
# Kind of confused how this handles mapping to itself with different chars
# Looks like because the length of the set for foo would be 2 and bar would be 3 would send the false
def isIsomorphic(s,t):
    return len(set(s))==len(set(zip(s,t)))==len(set(t))

# print(isIsomorphic("egg", "add"))
# print(isIsomorphic("foo", "bar"))
# print(isIsomorphic("paper", "title"))
# print(isIsomorphic("babc", "baba"))

"""
392. Is Subsequence
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

def isSubsequence(s, t):
    # Catches blanks
    if s == "":
        return True
    
    i = 0
    for char in t:
        if char == s[i]:
            i += 1
        if i == len(s):
            break
    return i == len(s)

print(isSubsequence("abc", "ahbgdc") == True)
print(isSubsequence("aec", "abcde") == False)
print(isSubsequence("axc", "ahbgdc") == False)
print(isSubsequence("aaaaaa", "bbaaaa") == False)
print(isSubsequence("", "") == True)
print(isSubsequence("bb", "ahbgdc") == False)
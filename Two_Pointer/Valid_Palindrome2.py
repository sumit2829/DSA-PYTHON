# Brute Force:
"""
def isPal(t):
    i = 0
    j = len(t) - 1

    while i < j:
        if t[i] != t[j]:
            return False
        i += 1
        j -= 1

    return True


def validPalindrome(s):
    if isPal(s):
        return True

    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if isPal(t):
            return True

    return False


s = "aca"
print(validPalindrome(s))

"""
# optimal
def ispal(s, si, ei):
    while si < ei:
        if s[si] != s[ei]:
            return False
        si += 1
        ei -= 1
    return True


def validPalindrome(s):
    si = 0
    ei = len(s) - 1

    while si < ei:
        if s[si] != s[ei]:
            return ispal(s, si + 1, ei) or ispal(s, si, ei - 1)
        si += 1
        ei -= 1

    return True


s = "aca"
print(validPalindrome(s))
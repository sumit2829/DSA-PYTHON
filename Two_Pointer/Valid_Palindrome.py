# Brute Force:
'''
def isPalindrome(s):
    t = ""

    for c in s:
        if c.isalnum():
            t += c.lower()

    rev = t[::-1]

    return t == rev

s = "was it a car or acat I saw"
print(isPalindrome(s))
'''

# Better
def isPalindrome(s):
    t = ""

    for c in s:
        if c.isalnum():
            t += c.lower()

    i = 0
    j = len(t)-1
    while i < j:
        if t[i] != t[j]:
            return False
        i+=1
        j-=1
    return True

s = "was it a car or acat I saw"
print(isPalindrome(s))
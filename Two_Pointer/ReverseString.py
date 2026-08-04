# Brute force:
"""
def reversestr(s):
    temp = []
    for i in range(len(s)-1,-1,-1):
        temp.append(s[i])
    return temp
s = ["n","e","e","t"]
print(reversestr(s))
"""

# Better Approach
"""
def reverseStr(s):
    i = 0
    j = len(s)-1
    
    while i < j:
        s[i],s[j] = s[j],s[i]
        i+=1
        j-=1
    return s
s = ["n","e","e","t"]
print(reverseStr(s))
"""

#  Optimal:
s = ["n","e","e","t"]
ans = reversed(s)
print(s)
    
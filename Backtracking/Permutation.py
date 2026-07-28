def permutation(s,curr=" "):
    if(len(s) == 0):
        print(curr)
        return
    for i in range(len(s)):
        ch = s[i]
        rem = s[:i] + s[i+1:]
        permutation(rem,curr+ch)
        
s = "abc"
permutation(s)
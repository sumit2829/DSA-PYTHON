def findSubset(s,curr=" ",index=0):
    if(index == len(s)):
        if curr == " ":
            print("Null")
        else:
            print(curr)
        return
    # incluse
    findSubset(s,curr+s[index],index+1)
    
    # exclude
    findSubset(s,curr,index+1)
    
s = "abc"
findSubset(s)
            
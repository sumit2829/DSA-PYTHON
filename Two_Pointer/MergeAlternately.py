# Brute Force
"""
def MergeAlt(word1, word2):
    res = ""
    i = 0
    j = 0

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            res += word1[i]
            i += 1

        if j < len(word2):
            res += word2[j]
            j += 1

    return res


word1 = "abc"
word2 = "xyz"
print(MergeAlt(word1, word2))
"""

# optimal

def mergeAlternately(word1, word2):
    i = 0
    j = 0
    res = []

    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1

    # Add remaining characters
    while i < len(word1):
        res.append(word1[i])
        i += 1

    while j < len(word2):
        res.append(word2[j])
        j += 1

    return "".join(res)


word1 = "abc"
word2 = "xyzv"

print(mergeAlternately(word1, word2))
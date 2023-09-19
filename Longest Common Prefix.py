# Link to submission:
[https://leetcode.com/problems/longest-common-prefix/submissions/1053434626/]

# Link to problem:
[https://leetcode.com/problems/longest-common-prefix/]


def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    strs.sort(key=len) 
    word = strs[0]
    comb = []
    
    for i in range(1, len(word)+1):
            comb.append(word[0:i])
    comb.sort(key=len, reverse=True)

    well = False
    for i in range(len(comb)):
        for k in range(1, len(strs)):
            if strs[k][0:len(comb[i])] == comb[i]:
                well = True  
                continue      
            else:
                well = False
                break
        if well:
            return comb[i]
        else:
            continue
    return ""


# Example:
strs = ["fdfvsrd", "fdfv", "fdfvjhefdkaejh", "fdfvtsdsa"]
print(longestCommonPrefix(strs))

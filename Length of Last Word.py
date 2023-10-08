# Link to submission:
    # https://leetcode.com/problems/length-of-last-word/submissions/1070090603/

# Link to problem:
    # https://leetcode.com/problems/length-of-last-word/description/
    

def lengthOfLastWord(s):
    n, l = None, 0   
    for i in range(len(s)-1, -1, -1):
        if s[i] == ' ':
            n = i
        else:
            break
    if not n:
        n = len(s)
    for i in range(n-1, -1, -1):          
        if s[i] != ' ':
            l += 1
        if s[i] == ' ':
            break
    return  l


# Example:
s = "world"

print(lengthOfLastWord(s))






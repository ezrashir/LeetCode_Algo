# Link to submission:
    # https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/1064128763/?envType=daily-question&envId=2023-10-01

# Link to problem:
    # https://leetcode.com/problems/reverse-words-in-a-string-iii/description/?envType=daily-question&envId=2023-10-01
    

def reverseWords(s):
    dict = {}
    new = ''
    k = 0
    t=0
    while k < len(s):
        while s[k] != ' ':
            if k==len(s)-1:
                k += 1
                break
            k += 1
        word = s[t:k]
        new += ' ' + word[::-1]
        k += 1   
        t = k
    return new[1:]


# Example:
s = 'Find your own path'
print(reverseWords(s))
    
    
    
    
    
    

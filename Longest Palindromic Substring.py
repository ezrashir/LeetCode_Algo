# Link to submission:
    # https://leetcode.com/problems/longest-palindromic-substring/submissions/1086882482/

# Link to problem:
    # https://leetcode.com/problems/longest-palindromic-substring/description/
    

def longestPalindrome(s): 
    
    def isPalindrome(s):
        if len(s)%2 == 0:
            for i in range(int(len(s)/2)):
                if s[i]!=s[-1-i]:
                    return False
        else:
            for i in range(int(len(s)/2)):
                if s[i]!=s[-1-i]:
                    return False       
        return True

    for i in range(len(s), 0, -1):
        for j in range(len(s)-i+1):
                if isPalindrome(s[j:i+j]):
                    return s[j:i+j]
    return s[0] 
    
    
# Example:
s = 'abbabbgag'  # res: 'bbabb'
print(longestPalindrome(s))









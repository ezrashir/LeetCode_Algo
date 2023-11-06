# Link to submission:
    # https://leetcode.com/problems/zigzag-conversion/submissions/1092677493/

# Link to problem:
    # https://leetcode.com/problems/zigzag-conversion/description/
    

def convert(s, numRows):
    if numRows == 1:
        return s
    
    rev = False
    result = [[] for i in range(numRows)]
    x = 0
    for i in range(len(s)):
        if rev == False: #regular order - increase row num
            result[x].append(s[i])
            x += 1
        else: #o opposite order - decrease row num
            result[x].append(s[i])
            x -= 1
            
        if x == numRows:
            rev = True
            x -= 2
        if x == 0:
            rev = False
                
    result = sum(result, [])
    return ''.join(result)


    
# Example:
s = 'IAMTRYINGTOFLOAT'
numRows = 5
print(convert(s, numRows))






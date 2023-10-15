# Link to submission:
    # https://leetcode.com/problems/add-binary/submissions/1075835936/

# Link to problem:
    # https://leetcode.com/problems/add-binary/description/
    

def addBinary(a, b): 
    
    if len(a) > len(b):
        maxi = a
        mini = b
    else:
        maxi = b
        mini = a
    
    sum = []
    sum[:] = maxi
    
    for i in range(-1, -len(mini)-1, -1):
        sum[i] = str(int(sum[i]) + int(mini[i]))
    
    for i in range(-1, -len(sum), -1):
        if sum[i] == '2':
            sum[i] = '0'
            sum[i-1] = str(int(sum[i-1]) + 1) 
        if sum[i] == '3':
            sum[i] = '1'
            sum[i-1] = str(int(sum[i-1]) + 1) 
            
    if sum[0] == '2':
        sum[0] = '0'
        sum = ['1'] + sum
    if sum[0] == '3':
        sum[0] = '1'
        sum = ['1'] + sum
        
    return ''.join(sum)
            
    
    
    
# Example:

a = str(110)
b = str(1101)
print(addBinary(a, b))






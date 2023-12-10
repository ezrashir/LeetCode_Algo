# Link to submission:
    # https://leetcode.com/problems/reverse-integer/submissions/1116396644/

# Link to problem:
    # https://leetcode.com/problems/reverse-integer/description/
    

def reverse(x: int) -> int:

    
    if x < 0:
        x = int(str(x)[:0:-1])
        return 0 if x > 2**31 else -x
    else:
        x = int(str(x)[::-1])
        return 0 if x > 2**31-1 else x

        
    
    
    
# Example:

x = -120
print(reverse(x))






# Link to submission:
    # https://leetcode.com/problems/plus-one/submissions/1072597343/

# Link to problem:
    # https://leetcode.com/problems/plus-one/description/
    

def plusOne1(digits): 
    if len(digits) == 1:
        if digits[0] == 9:
            digits[0] = 0
            return [1] + digits
        else:
            return [digits[0]+1]
    else:    
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            temp = plusOne1(digits[:-1])
            return temp + [0]


def plusOne2(digits): 
    if digits[-1] == 9:
        loc = -1
        for i in range(len(digits)):
            if digits[i] != 9:
                loc = i 
        if loc != -1:
            return [digits[i] for i in range(loc)] + [digits[loc]+1] + [0 for i in range(len(digits)-loc-1)]            
        else:
            return [1] + [0 for i in range(len(digits))]
    else:
        digits[-1] += 1
        return digits

 
   


# Example:
digits = [1, 9, 9, 1, 9, 9]
print(plusOne1(digits))
print(plusOne2(digits))






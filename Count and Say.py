# Link to submission:
    # https://leetcode.com/problems/count-and-say/submissions/1063992335/

# Link to problem:
    # https://leetcode.com/problems/count-and-say/description/
    

def countAndSay(n):       
    def Say(num):
        str0 = ''
        if num==1:
            return '1' + str(num)
        else:
            k_tot = 0
            while k_tot < len(num):
                k = 1
                if k+k_tot == len(num):
                    return str0 + '1' + num[-1]  
                else:
                    while num[k+k_tot-1] == num[k+k_tot]:
                        k += 1
                        if k+k_tot >= len(num):
                            return str0 + str(k) + num[-1]  
                str0 += str(k) + str(num[k_tot + k-1])
                k_tot += k
        return str0

    if n == 1:
        return n
    else:
        return Say(countAndSay(n-1))


# Example:
n = 5
print(countAndSay(n))






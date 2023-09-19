# Link to submission:
    # https://leetcode.com/problems/roman-to-integer/submissions/1053397274/

# Link to problem:
    # https://leetcode.com/problems/roman-to-integer/



class Solution():
    def romanToInt(self, s:str):
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        temp = 0
        for i in range(len(s)-1):
            if dict[s[i]] >= dict[s[i+1]]:
                temp += dict[s[i]]
            if dict[s[i]] < dict[s[i+1]]:
                temp -= dict[s[i]]
        temp += dict[s[-1]]
        return temp


# Example:
str = 'CCCXLIV'
roman = Solution()
print(roman.romanToInt(s=str))

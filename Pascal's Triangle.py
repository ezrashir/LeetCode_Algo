# Link to submission:
    # https://leetcode.com/problems/pascals-triangle/submissions/1153446557/

# Link to problem:
    # https://leetcode.com/problems/pascals-triangle/description/
    

def generate(numRows: int) -> list[list[int]]:
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        Ptree = [[1], [1, 1]]
        for row in range(2, numRows):
            Ptree.append([1 if i==0 or i==row else Ptree[row-1][i-1]+Ptree[row-1][i] for i in range(row+1)])
        return Ptree

    
# Example:
n = 30
print(generate(n))






# Link to submission:
    # https://leetcode.com/problems/remove-element/submissions/1059508136/

# Link to problem:
    # https://leetcode.com/problems/remove-element/description/


def removeElement(nums, val):
    inx = 0
    for i in range(len(nums)):
        if nums[i] != val:
           nums[inx] = nums[i]
           inx += 1  
    return inx, nums



# Example:
val = 0
nums = [3,3,0,1,1,1,2,0,0,2,3,3,4]
print(removeElement(nums, val))
# Link to submission:
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

# Link to problem:
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/


def removeDuplicates(nums):
    inx = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
           nums[inx] = nums[i]
           inx += 1  
    return inx, nums


# Example:
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
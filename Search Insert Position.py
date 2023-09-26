# Link to submission:
    # https://leetcode.com/problems/search-insert-position/submissions/

# Link to problem:
    # https://leetcode.com/problems/search-insert-position/
    

def searchInsert(nums, target):
        if not nums:
            return 0
        mid = len(nums)//2
        if nums[mid] < target:
            return mid + 1 + searchInsert(nums[mid+1:], target)
        elif nums[mid] > target:
            return searchInsert(nums[:(mid)], target)
        else:
            return mid


# Example:
nums = [0,1,2,3,4,5,6,7,8,9,10]
target = 4
print(searchInsert(nums, target))
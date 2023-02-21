"""
704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

def search(nums, target):
    try:
        return nums.index(target)
    except:
        return -1

# O(log n), thats this
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1        
    return -1    
    
print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))
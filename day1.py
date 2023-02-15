"""
1480. Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
"""

def runningSum(nums):
    finArr = []
    for index, value in enumerate(nums):
        if index == 0:
            finArr.append(value)
        else:
            finArr.append(value + finArr[index - 1])
    return finArr

print(runningSum([1,2,3,4]) == [1,3,6,10])
print(runningSum([1,1,1,1,1]) == [1,2,3,4,5])
print(runningSum([3,1,2,10,1]) == [3,4,6,16,17])

"""
724. Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
"""

def pivotIndex(nums):
    for index in range(len(nums)):
        if index == 0:
            if sum(nums[1:]) == 0:
                return 0
        else:
            if sum(nums[index+1:]) == sum(nums[:index]):
                return index
    return -1

print(pivotIndex([2,1,-1]) == 0)
print(pivotIndex([1,2,3]) == -1)
print(pivotIndex([1,7,3,6,5,6]) == 3)

# This solution was significantly faster
# Never would have written this, damn was this clever.
def pivotIndex(nums):
        L = 0
        # This is the total sum of the arr
        R = sum(nums)
        for i in range(len(nums)):
            # Looks like they subtract the index value from the right "sum" 
            R -= nums[i]
            # Check if its equivalent
            if L == R:
                return i
            # Adds the index value to the left then reiterates
            L += nums[i]
        # Nothing matches then return -1
        return -1
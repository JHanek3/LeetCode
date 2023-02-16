import numpy as np
"""
1523. Count Odd Numbers in an Interval Range
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
"""

def countOdds(low, high):
    # If N is even then the count of both odd and even numbers with be N / 2
    n = (high - low) // 2
    
    if low % 2 != 0 or high % 2 != 0:
        n += 1
    return n  


print(countOdds(0, 10) == 5)
print(countOdds(3, 7) == 3)
print(countOdds(0, 10) == 1)

"""
1491. Average Salary Excluding the Minimum and Maximum Salary
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary. Answers within 10^-5 of the actual answer will be accepted.
"""
def average(salary):
    sortedArr = np.sort(salary)[1:len(salary) - 1]
    return np.average(sortedArr)

print(average([4000,3000,1000,2000]) == 2500.00000)
print(average([1000,2000,3000]) == 2000.00000)

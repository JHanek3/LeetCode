import sys
"""
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

# How I solved it, times out.
# I solved it with two for loops

def maxProfit(prices):
    maxProfit = 0
    minValue = sys.maxsize

    for price in prices:
        # If we have a new minValue set the minValue
        if price < minValue:
            minValue = price
        # If the price is not a new minValue check it minus the minValue to see
        # if its a new max profit
        elif price - minValue > maxProfit:
            maxProfit = price - minValue

    return maxProfit

maxProfit([7,1,5,3,6,4])
maxProfit([7,6,5,4,3,1])
maxProfit([2,4,1])

"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    letters = {}

    for char in s:
        if char not in letters.keys():
            letters[char] = 1
        else:
            letters[char] += 1

    res = 0
    odd = 0

    # accounts for aaaaaaaaaaaaaaaa
    if len(letters) == 1:
        return letters[s[0]]
    
    for i in letters.values():
        if i > 1:
            if i % 2 == 0:
                res += i
            else:
                res += i - 1
                odd += 1
        else:
            odd += 1
    
    if odd > 0:
        res += 1
    
    return res
"""
Thats fun, so insted of just constantly adding a value to odd like above
it just turns on a bool flag and just adds 1 in the return statement

len_ = 0
isOdd = False
for count in hmap.values():
    if count%2==0:
        len_ +=count
    else:
        len_+=(count-1)
        is_odd = True

return len_+1 if is_odd else len_
"""
    
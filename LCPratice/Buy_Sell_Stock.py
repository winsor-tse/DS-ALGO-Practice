"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""


if __name__ == "__main__":
    """
    Assumptions: max(profit) -> 2 or 6 choose 6
                 there is more than one price -> if there is one return 0 -> base case
    
    [7,3,5,1,6,4] -> BF O(n^2) -> double for loop

    O(n)
    7   1
    #t
    curr_index = 0
    next index = 1
    sum count = 1 - 7 = -6
---
    curr index = 1 -> loest value
    next index = 2
    sum count 5-1 = 4 -> max function return max

    """
    #Time Complexity: O(n) n is the length of the array
    #Space Complexity: O(n) if not in function O(1 in function)
    arr = [7,1,5,3,6,4]
    index = 0
    curr_lowest = arr[0]
    sum_count = 0
    profit = 0
    if len(arr) == 0:
        print(0)
    while index < len(arr)-1:
        sum_count = arr[index+1] - curr_lowest
        profit = max(sum_count,profit)
        curr_lowest = min(index,index+1)
        index+=1
    print(profit)
    print('hello')
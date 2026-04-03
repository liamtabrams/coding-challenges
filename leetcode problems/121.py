"""
121. Best Time to Buy and Sell Stock
Attempted
Easy

Topics

Companies
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
class Solution:
    """
    Variant 1:
    The official solution given by LC for 'Approach 1: Brute Force', which results in a
    Time Limit Exceeded Answer. The time complexity of this solution is O(n^2) where n
    is the length of 'prices' because of the nested for loop (though because of the
    restriction on the range for j as a function of i, the number of iterations of the
    nested for loop is actually closer to n^2/2), and the space complexity is O(1) since
    the amount of memory used does not depend on n. 
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit


class Solution:
    """
    Variant 2:
    The official solution given by LC for Approach 2: 'One Pass'. It was definitely
    frustrating that I was not able to come up with this solution on my own, 
    especially considering this is categorized as an 'Easy' problem, but I
    think it has just been a rough Monday for me with plenty of distractions. Anyway,
    the run time complexity of this solution is O(n), and the space complexity of this
    solution is O(1). This solution beats ~78% and ~45% of accepted answers in terms
    of run time and memory efficiency, respectively. 
    """
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit
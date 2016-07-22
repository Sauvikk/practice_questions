# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Example :
#
# Input : [1 2 1 2]
# Output : 2
#
# Explanation :
#   Day 1 : Buy
#   Day 2 : Sell
#   Day 3 : Buy
#   Day 4 : Sell

# sol for k transactions can be found here :
# https://leetcode.com/discuss/15153/a-clean-dp-solution-which-generalizes-to-k-transactions


class Solution:
    def sol(self, price):

        if price is None or len(price) < 2:
            return 0
        left = [0] * len(price)
        right = [0] * len(price)

        left[0] = 0
        minimum = price[0]
        for i in range(len(price)):
            minimum = min(minimum, price[i])
            left[i] = max(left[i-1], price[i] - minimum)

        right[len(price)-1] = 0
        maximum = price[-1]
        for i in range(len(price)-2, -1, -1):
            maximum = max(maximum, price[i])
            right[i] = max(right[i+1], maximum - price[i])
        profit = 0
        for i in range(len(price)):
            profit = max(profit, right[i]+left[i])
        return profit


c = [1, 2, 1, 2]
print(Solution().sol(c))

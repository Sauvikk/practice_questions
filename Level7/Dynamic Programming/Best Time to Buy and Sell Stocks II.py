# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like (ie, buy one
# and sell one share of the stock multiple times). However, you may not engage
# in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Example :
#
# Input : [1 2 3]
# Return : 2


class Solution:
    def sol(self, price):
        profit = 0
        for i in range(1, len(price)):
            diff = price[i] - price[i - 1]
            if diff > 0:
                profit += diff
        return profit


c = [100, 180, 260, 310, 40, 535, 695]
print(Solution().sol(c))

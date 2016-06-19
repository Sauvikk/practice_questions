# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example :
#
# Input : [1 2]
# Return :  1


class Solution:
    def sol(self, price):
        minimum = price[0]
        result = 0
        for i in range(1, len(price)):
            result = max(result, price[i] - minimum)
            minimum = min(minimum, price[i])
        return result

c = [100, 180, 260, 310, 40, 535, 695]
print(Solution().sol(c))

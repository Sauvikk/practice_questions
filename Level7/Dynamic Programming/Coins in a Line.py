# There are N coins (Assume N is even) in a line.
# Two players take turns to take a coin from one of the ends of the line until there are no more coins left.
# The player with the larger amount of money wins. Assume that you go first.
#
# Write a program which computes the maximum amount of money you can win.
#
# Example:
#
# suppose that there are 4 coins which have value
# 1 2 3 4
# now you are first so you pick 4
# then in next term
# next person picks 3 then
# you pick 2 and
# then next person picks 1
# so total of your money is 4 + 2 = 6
# next/opposite person will get 1 + 3 = 4
# so maximum amount of value you can get is 6
# http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/


class Solution:

    def sol(self, coin):
        n = len(coin)
        dp = [[0 for x in range(n)] for x in range(n)]
        for gap in range(0, n):
            for i, j in zip(range(n), range(gap, n)):
                x = dp[i+2][j] if i+2 <= j else 0
                y = dp[i+1][j-1] if i+1 <= j-1 else 0
                z = dp[i][j-2] if i <= j-2 else 0
                dp[i][j] = max(coin[i] + min(x, y), coin[j] + min(y, z))
        return dp[0][n-1]

xx = [1, 2, 3, 4]
print(Solution().sol(xx))

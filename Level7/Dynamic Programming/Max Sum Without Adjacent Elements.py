# Given a 2 * N Grid of numbers, choose numbers such that the sum of the numbers
# is maximum and no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.
#
# Example:
#
# Grid:
# 	1 2 3 4
# 	2 3 4 5
# so we will choose
# 3 and 5 so sum will be 3 + 5 = 8
#
#
# Note that you can choose more than 2 numbers


class Solution:

    def sol(self, grid):
        m = len(grid[0])
        dp = [0]*m
        dp[0] = max(grid[0][0], grid[1][0])
        if m == 1:
            return dp[0]
        dp[1] = max(grid[0][1], grid[1][1], dp[0])
        for i in range(2, m):
            temp = max(grid[0][i], grid[1][i])
            dp[i] = max(temp+dp[i-2], dp[i-1], temp)
        return dp[m-1]

x = [
  [1, 2, 3, 4],
  [2, 3, 4, 5]
]
print(Solution().sol(x))


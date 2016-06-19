# Given a m x n grid filled with non-negative numbers, find a path
# from top left to bottom right which minimizes the sum of all numbers along its path.
#
#  Note: You can only move either down or right at any point in time.
# Example :
#
# Input :
#
#     [  1 3 2
#        4 3 1
#        5 6 1
#     ]
#
# Output : 8
#      1 -> 3 -> 2 -> 1 -> 1


class Solution:
    def sol(self, grid):
        if grid is None or len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for x in range(n)] for x in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1, m):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[m-1][n-1]


c = [
    [20, 29, 84, 4, 32, 60, 86, 8, 7, 37],
    [77, 69, 85, 83, 81, 78, 22, 45, 43, 63],
    [60, 21, 0, 94, 59, 88, 9, 54, 30, 80],
    [40, 78, 52, 58, 26, 84, 47, 0, 24, 60],
    [40, 17, 69, 5, 38, 5, 75, 59, 35, 26],
    [64, 41, 85, 22, 44, 25, 3, 63, 33, 13],
    [2, 21, 39, 51, 75, 70, 76, 57, 56, 22],
    [31, 45, 47, 100, 65, 10, 94, 96, 81, 14]
]
print(Solution().sol(c))

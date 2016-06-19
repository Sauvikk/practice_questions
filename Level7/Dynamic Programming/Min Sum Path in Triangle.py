# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
#  Note:
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.


class Solution:
    def sol(self, triangle):
        total = [0] * len(triangle)
        last_row = len(triangle)-1
        for i in range(len(triangle[last_row])):
            total[i] = triangle[last_row][i]
        for i in range(last_row-1, -1, -1):
            for j in range(0, len(triangle[i])):
                total[j] = triangle[i][j] + min(total[j], total[j+1])
        return total[0]


c = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
res = Solution().sol(c)
print(res)

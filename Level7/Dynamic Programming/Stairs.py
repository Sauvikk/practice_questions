# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example :
#
# Input : 3
# Return : 3
#
# Steps : [1 1 1], [1 2], [2 1]


class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        f1 = 1
        f2 = 2
        if n < 3:
            return n
        for i in range(3, n + 1):
            f2 = f1 + f2
            f1 = f2 - f1
        return f2

print(Solution().climbStairs(3))

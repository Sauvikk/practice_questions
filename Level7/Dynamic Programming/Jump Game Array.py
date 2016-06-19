# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return 1 ( true ).
#
# A = [3,2,1,0,4], return 0 ( false ).
#
# Return 0/1 for this problem


class Solution:
    def sol(self, A):
        farthest = 0
        for i in range(len(A)-1):
            farthest = max(farthest, i + A[i])
            if farthest == i:
                return 0
        return 1

c = [2, 3, 1, 1, 4]
c1 = [3, 2, 1, 0, 4]
print(Solution().sol(c1))

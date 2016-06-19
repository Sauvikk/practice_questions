# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example :
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2.
# (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#
# If it is not possible to reach the end index, return -1.
# http://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
# dp solution, works for get the jumping positions


class Solution:
    def sol(self, A):
        jumps = [0] * len(A)
        if len(A) == 1:
            return 1
        if len(A) == 0 or A[0] == 0:
            return -1
        jumps[0] = 0
        for i in range(1, len(A)):
            jumps[i] = -1
            for j in range(0, i):
                if i <= j + A[j] and jumps[j] != -1:
                    jumps[i] = max(jumps[i], jumps[j] + 1)
                    break
        return jumps[len(A) - 1]


c = [2, 3, 1, 1, 4]
c1 = [3, 2, 1, 0, 4]
print(Solution().sol(c))

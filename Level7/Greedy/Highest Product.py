# Given an array of integers, return the highest product possible by multiplying 3 numbers from the array
#
# Input:
#
# array of integers e.g {1, 2, 3}
#  NOTE: Solution will fit in a 32-bit signed integer
# Example:
#
# [0, -1, 3, 100, 70, 50]
#
# => 70*50*100 = 350000


class Solution:

    def sol(self, arr):
        arr.sort()
        return max((arr[0]*arr[1]*arr[-1]), (arr[-1]*arr[-2]*arr[-3]))

res1 = Solution().sol([0, -1, 3, 100, 70, 50])
print(res1)
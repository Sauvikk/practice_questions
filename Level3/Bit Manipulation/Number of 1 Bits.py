# Write a function that takes an unsigned integer and returns the number of 1 bits it has.
#
# Example:
#
# The 32-bit integer 11 has binary representation
#
# 00000000000000000000000000001011
# so the function should return 3.
#
# Note that since Java does not have unsigned int, use long for Java
# http://articles.leetcode.com/reverse-bits/
# http://www.geeksforgeeks.org/write-an-efficient-c-program-to-reverse-bits-of-a-number/


import sys


class Solution:

  def solution(self, x):
        n = sys.getsizeof(x) * 8
        for i in range(int(n/2)):
            x = self.swapbits(x, i, n-1-i)
        return x

  def swapbits(self, x, i, j):
        # print(i, (x >> i) & 1) gives ith bit
        # print(j, (x >> j) & 1) gives jth bit
        start = (x >> i) & 1
        end = (x >> j) & 1
        if start ^ end:
            x ^= (1 << i) | (1 << j)
        return x


x = 3
res = Solution().solution(x)
print(res)

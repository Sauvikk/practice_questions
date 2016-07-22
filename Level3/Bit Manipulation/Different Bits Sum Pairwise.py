# We define f(X, Y) as number of different corresponding bits
# in binary representation of X and Y. For example, f(2, 7) = 2, since binary
# representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.
#
# You are given an array of N positive integers, A1, A2 ,…, AN.
# Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.
#
# For example,
#
# A=[1, 3, 5]
#
# We return
#
# f(1, 1) + f(1, 3) + f(1, 5) +
# f(3, 1) + f(3, 3) + f(3, 5) +
# f(5, 1) + f(5, 3) + f(5, 5) =
#
# 0 + 1 + 1 +
# 1 + 0 + 2 +
# 1 + 2 + 0 = 8
# http://stackoverflow.com/questions/32996527/recent-google-interview-puzzle-on-bitwise-operation


class Solution:

  def solution(self, arr):
        sum = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                sum += self.count_diff_bits(arr[i], arr[j])
        return 2 * sum

  def count_diff_bits(self, a, b):
        x = a ^ b
        return self.numSetBits(x)

  def numSetBits(self, x):
        count = 0
        while x != 0:
              x &= (x - 1)
              count += 1
        return count

arr = [1, 3, 5]
res = Solution().solution(arr)
print(res)

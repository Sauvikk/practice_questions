# http://www.geeksforgeeks.org/rearrange-given-array-place/
import math


class Solution:

  @staticmethod
  def solution(s):
        n = len(s)
        rank = 1
        for i in range(n-1):
            x = 0
            for j in range(i+1, n):
                if s[i] > s[j]:
                    x += 1
            rank += x * math.factorial(n-i-1)
            rank %= 1000003
        return rank

s = "caff"
output = Solution.solution(s)
print(output)


import math


class Solution:

  @staticmethod
  def solution(n):
        size = len(n) - 1
        res = 0
        power = 0
        while size >= 0:
            curr_char = n[size]
            res += int(math.pow(26, power) * (ord(curr_char) - ord('A') + 1))
            size -= 1
            power += 1
        return res

a = 'AAC'
res = Solution.solution(a)
print(res)

import math


class Solution:

  @staticmethod
  def solution(a):
        res = []
        for i in range(1, int(math.sqrt(a))+1):
            if a % i == 0:
                res.append(i)
                if i != math.sqrt(a):
                    res.append(a/i)
        res.sort()
        return res

a = 25
res = Solution.solution(a)
print(res)

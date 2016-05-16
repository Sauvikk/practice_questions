import math


class Solution:

  @staticmethod
  def solution(a):
        res = []
        for i in range(a+1):
            res.append(1)
        res[0] = 0
        res[1] = 0
        for i in range(2, int(math.sqrt(a))+1):
            if res[i] == 1:
                for j in range(2, a):
                    if (i*j) > a:
                        break
                    res[i*j] = 0
        prime = []
        for i in range(a+1):
            if res[i] == 1:
                prime.append(i)
        return prime
a = 50
res = Solution.solution(a)
print(res)

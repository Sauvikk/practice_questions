class Solution:

  @staticmethod
  def solution(m, n):
        if m < n:
            return Solution.solution(n, m)
        elif n == 0:
            return m
        else:
            return Solution.solution(n, m % n)
m = 3
n = 1
res = Solution.solution(m, n)
print(res)

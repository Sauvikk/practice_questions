class Solution:

  @staticmethod
  def solution(n):
        res = []
        binary = ""
        if n == 0:
            return "0"
        while n > 0:
            rem = n % 2
            res.append(rem)
            n = int(n/2)
        for i in range(len(res)-1, -1, -1):
            binary += str(res[i])
        return binary

a = 9
res = Solution.solution(a)
print(res)

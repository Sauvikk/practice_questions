class Solution:

  @staticmethod
  def solution(n):
        ret = ''
        while n != 0:
            n -= 1
            rem = n%26
            n = int(n/26)
            ret += chr(rem+ord('A'))
        return ret[::-1]

a = 705
res = Solution.solution(a)
print(res)

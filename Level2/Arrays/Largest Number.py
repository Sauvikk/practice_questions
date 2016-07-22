from fractions import Fraction


class Solution:

  @staticmethod
  def solution(a):
        res = ""
        a = sorted(a, key=lambda n: Fraction(n, 10**len(str(n))-1), reverse=True)
        while a[0] == 0 and len(a) != 1:
            del a[0]
        print(a)
        for num in a:
            res += str(num)
        return res

a = [12, 121]
res = Solution.solution(a)
print(res)

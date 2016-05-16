# http://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
class Solution:

  @staticmethod
  def solution(A):
        count = 0
        i = 5
        while A/i != 0:
            count += int(A/i)
            i *= 5
        return count

a = 5487
res = Solution.solution(a)
print(res)

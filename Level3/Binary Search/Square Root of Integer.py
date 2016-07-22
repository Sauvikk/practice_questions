# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# If x is not a perfect square, return floor(sqrt(x))


class Solution:

  @staticmethod
  def solution(a):
        low = 0
        high = a
        while low <= high:
            mid = int((low+high)/2)
            res = mid * mid
            if res == a:
                return int(mid)
            elif res > a:
                high = mid - 1
            else:
                low = mid + 1
        return int(high)

a = 16
res = Solution.solution(a)
print(res)

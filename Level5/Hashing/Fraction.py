# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# Example :
#
# Given numerator = 1, denominator = 2, return "0.5"
# Given numerator = 2, denominator = 1, return "2"
# Given numerator = 2, denominator = 3, return "0.(6)"


class Solution:

  @staticmethod
  def solution(n, d):
        if n == 0:
            return 0
        res = []
        if (n < 0 or d < 0) and (n * d < 0):
            res.append(str('-'))
        n = abs(n)
        d = abs(d)
        res.append(str(int(n/d)))
        if n % d == 0:
            return ''.join(res)
        res.append('.')
        map = {}
        r = n % d
        while r:
            if r in map:
                res.insert(map[r], '(')
                res.append(')')
                break
            map[r] = len(res)
            r *= 10
            res.append(str(int(r/d)))
            r = r % d
        return ''.join(res)
res1 = Solution.solution(100, -2)
print(res1)

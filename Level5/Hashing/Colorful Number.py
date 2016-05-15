# For Given Number N find if its COLORFUL number or not
#
# Return 0/1
#
# COLORFUL number:
#
# A number can be broken into different sub-sequence parts.
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# And this number is a COLORFUL number, since product of every digit of a sub-sequence are different
# Example:
#
# N = 23
# 2 3 23
# 2 -> 2
# 3 -> 3
# 23 -> 6
# this number is a COLORFUL number since product of every digit of a sub-sequence are different.
#
# Output : 1


class Solution:

  @staticmethod
  def solution(num):
        s = str(num)
        res = {}
        for k in range(len(s)):
            for i in range(k, len(s)):
                j = k
                prod = 1
                while j < i + 1:
                    prod *= int(s[j])
                    j += 1
                if prod in res:
                    return False
                else:
                    res[prod] = 1
        return True
number = 23
res1 = Solution.solution(number)
print(res1)


# Implement pow(x, n) % d.
#
# In other words, given x, n and d,
#
# find (x^n % d)
#
# Note that remainders on division cannot be negative.
# In other words, make sure the answer you return is non negative.


# Input : x = 2, n = 3, d = 3
# Output : 2
#
# 2^3 % 3 = 8 % 3 = 2

# sys.setrecursionlimit(1500) recursion is not working


class Solution:

   def power(self, x, n, d):
       ans = 1
       base = x
       if n == 0:
           return 1 % n
       while n > 0:
           if n % 2 == 1:
               ans = (ans * base) % d
               n -= 1
           else:
               base = (base * base)%d
               n = int(n/2)
       return int((ans + d) % d)


x = 2
n = 3
d = 3
res = Solution().power(x, n, d)
print(res)

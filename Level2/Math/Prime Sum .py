import math


class Solution:

  @staticmethod
  def solution(n):
        res = []
        prime = []
        for i in range(n+1):
            prime.append(1)
        prime[0] = 0
        prime[1] = 0
        limit = int(math.sqrt(n))
        for i in range(2, limit + 1):
            if prime[i] == 1:
                for j in range(2, n):
                    if (i * j) > n:
                        break
                    prime[i*j] = 0
        for i in range(2, len(prime)):
            if prime[i] == 1 and prime[n-i] == 1:
                res.append(i)
                res.append(n-i)
                break
        return res

a = 16777214
res = Solution.solution(a)
print(res)


# more effiecient solution (always use xrange)

# import math
# class Solution:
#     # @param A : integer
#     # @return a list of integers
#     def primesum(self, n):
#         res = []
#         for i in xrange(2 , n):
#             if self.isPrime(i) and self.isPrime(n-i):
#                 res.append(i)
#                 res.append(n - i)
#                 return res
#
#     def isPrime(self, n):
#         if n < 2:
#             return False
#
#         for i in xrange(2, int(n**0.5)+1):
#             if n % i == 0:
#                 return False
#         return True
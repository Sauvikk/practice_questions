import math
import sys


class Solution:

  @staticmethod
  def solution(N):
        if N == 0:
            return False
        if N == 1:
            return True
        for A in range(2, int(math.sqrt(N))+1):
            P = math.log(N)/math.log(A)
            if P - int(P) < 0.000000001:
                print(P)
                print(int(P))
                return True
        return False
a = 536870912
res = Solution.solution(a)
print(res)


# class Solution:
#
#   @staticmethod
#   def solution(x):
#         if x <= 1:
#             return True
#         limit = math.sqrt(x)
#         for base in range(2, sys.maxsize+1):
#             if base >= x and base >= sys.maxsize/base:
#                 break
#             temp = base
#             while temp <= x and temp < sys.maxsize/base:
#                 print(str(temp) + "*" + str(base))
#                 temp *= base
#                 if temp == x:
#                     return True
#         return False
# a = 21474
# res = Solution.solution(a)
# print(res)


#  more efficient

# import sys
# import math
# class Solution:
#     # @param A : integer
#     # @return a boolean
#     def isPower(self, N):
#         if N == 0:
#             return False
#         if N == 1:
#             return True
#         for p in xrange(2,33):
#             for A in xrange(2, int(N**(1.0 / p)) + 2):
#                 if A**p == N:
#                     return True
#         return False

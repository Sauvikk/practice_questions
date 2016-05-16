class Solution:

  @staticmethod
  def solution(N):
        flag = False
        if N < 0:
            flag = True
            N = 0 - N
        rev = 0
        while N != 0:
            rev = rev*10 + N % 10
            N = int(N/10)
        if rev > 2**31-1:
            return 0
        if flag is True:
            rev = 0 - rev
        return rev
a = 2147483647
res = Solution.solution(a)
print(res)


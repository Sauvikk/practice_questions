# http://qa.geeksforgeeks.org/3676/number-of-unique-paths
class Solution:

  @staticmethod
  def solution(m, n):
        ans = 1
        i = n
        while i < (m + n -1):
            ans *= i
            ans = int(ans/(i - n + 1))
            i += 1
        return ans

m = 2
n = 2
res = Solution.solution(m, n)
print(res)



# def uniquePaths(self, A, B):
#         return math.factorial(A+B-2)/(math.factorial(A-1)*math.factorial(B-1))
class Solution:

  @staticmethod
  def solution(n):
        if n < 0:
            return False
        div = 1
        while n/div >= 10:
            div *= 10
        while n != 0:
            left = int(n/div)
            right = n % 10
            if left != right:
                return False
            n = int((n % div)/10)
            div /= 100
        return True
n = 0
res = Solution.solution(n)
print(res)




# class Solution:
#     # @param A : integer
#     # @return an integer
#     def isPalindrome(self, A):
#         A = str(A)
#         for i in range(len(A)/2+1):
#             if A[i] != A[-(i+1)]:
#                 return 0
#         return 1

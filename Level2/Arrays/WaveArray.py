class Solution:

  @staticmethod
  def solution(a):
        a.sort()
        for i in range(0, len(a)-1, 2):
                a[i], a[i+1] = a[i+1], a[i]
        return a


a = [5, 1, 3, 2, 4]
res = Solution.solution(a)
print(res)

# less time complexity
# class Solution:
#
#   @staticmethod
#   def solution(a):
#         for i in range(0, len(a), 2):
#             if i > 0 and a[i] < a[i-1]:
#                     a[i], a[i-1] = a[i-1], a[i]
#             if i< len(a) - 1 and a[i] < a[i+1]:
#                     a[i], a[i+1] = a[i+1], a[i]
#         return a
#
#
# a = [ 5, 1, 3, 2, 4 ]
# res = Solution.solution(a)
# print(res)

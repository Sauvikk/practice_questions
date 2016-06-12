# Given an array, find the nearest smaller element G[i]
#  for every element A[i] in the array such that the element has an index smaller than i.
#
# More formally,
#
# G[i] for an element A[i] = an element A[j] such that
#     j is maximum possible AND
#     j < i AND
#     A[j] < A[i]
# Elements for which no smaller element exist, consider next smaller element as -1.
#
# Example:
#
# Input : A : [4, 5, 2, 10]
# Return : [-1, 4, -1, 2]
#
# Example 2:
#
# Input : A : [3, 2, 1]
# Return : [-1, -1, -1]



class Solution:

  @staticmethod
  def solution(arr):
        result = []
        stack = []
        for i in range(len(arr)):
            while len(stack) != 0 and stack[-1] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
            stack.append(arr[i])
        return result


arr = [4, 5, 2, 10]
res = Solution.solution(arr)
print(res)

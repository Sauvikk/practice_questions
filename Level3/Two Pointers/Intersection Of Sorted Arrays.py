# Find the intersection of two sorted arrays.
# OR in other words,
# Given 2 sorted arrays, find all the elements which occur in both the arrays.
#
# Example :
#
# Input :
#     A : [1 2 3 3 4 5 6]
#     B : [3 3 5]
#
# Output : [3 3 5]
#
# Input :
#     A : [1 2 3 3 4 5 6]
#     B : [3 5]
#
# Output : [3 5]
# NOTE : For the purpose of this problem ( as also conveyed by the sample case ),
# assume that elements that appear more than once in both arrays should be included multiple times in the final output.
# http://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/


class Solution:

  @staticmethod
  def solution(arr1, arr2):
            res = []
            i = 0
            j = 0
            size1 = len(arr1)
            size2 = len(arr2)
            while i < size1 and j <size2:
                if arr1[i] < arr2[j]:
                    i += 1
                elif arr2[j] < arr1[i]:
                    j += 1
                elif arr1[i] == arr2[j]:
                    res.append(arr1[i])
                    i += 1
                    j += 1
            return res

arr1 = [1, 2, 3, 3, 4, 5, 6]
arr2 = [3, 3, 5]
res = Solution.solution(arr1, arr2)
print(res)
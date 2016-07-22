# You are given 3 arrays A, B and C. All 3 of the arrays are sorted.
#
# Find i, j, k such that :
# max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
#
# **abs(x) is absolute value of x and is implemented in the following manner : **
#
#       if (x < 0) return -x;
#       else return x;
# Example :
#
# Input :
#         A : [1, 4, 10]
#         B : [2, 15, 20]
#         C : [10, 12]
#
# Output : 5
#          With 10 from A, 15 from B and 10 from C.


class Solution:

  @staticmethod
  def solution(arr1, arr2, arr3):
            i, size1 = 0, len(arr1)
            j, size2 = 0, len(arr2)
            k, size3 = 0, len(arr3)
            diff = 2 ** 31 - 1
            while i < size1 and j < size2 and k < size3:
                minimum = min(arr1[i], min(arr2[j], arr3[k]))
                maximum = max(arr1[i], max(arr2[j], arr3[k]))
                diff = min(diff, maximum - minimum)
                if diff == 0:
                    return diff
                elif arr1[i] == minimum:
                    i += 1
                elif arr2[j] == minimum:
                    j += 1
                else:
                    k += 1
            return diff

arr1 = [1, 4, 10]
arr2 = [2, 15, 20]
arr3 = [10, 12]
res = Solution.solution(arr1, arr2, arr3)
print(res)

# Remove duplicates from Sorted Array
# Given a sorted array,
# remove the duplicates in place such that each element appears only once and return the new length.
#
# Note that even though we want you to return the new length, make sure to change the original array as well in place
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
#  Example:
# Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2].


class Solution:

  @staticmethod
  def solution(arr):
            size = len(arr)
            if size == 0 or size == 1:
                    return size
            i = 1
            for j in range(1, size):
                    if arr[j] != arr[j - 1]:
                        arr[i] = arr[j]
                        i += 1
            if i < len(arr):
                del arr[i:]
            return i

arr = [1, 1, 2, 2, 3, 3, 3, 4, 4]
res = Solution.solution(arr)
print(arr)
print(res)



# def removeDuplicates(self, A):
#         prev = 0
#         curr = 1
#         size = len(A)
#         while curr < size:
#             if A[curr] == A[prev]:
#                 curr += 1
#             else:
#                 prev += 1
#                 A[prev] = A[curr]
#                 curr += 1
#         return prev + 1

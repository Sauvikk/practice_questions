# Given an array and a value, remove all the instances of that value in the array.
# Also return the number of elements left in the array after the operation.
# It does not matter what is left beyond the expected length.
#
#  Example:
# If array A is [4, 1, 1, 2, 1, 3]
# and value elem is 1,
# then new length is 3, and A is now [4, 2, 3]
# Try to do it in less than linear additional space complexity.

class Solution:

  @staticmethod
  def solution(arr, target):
            size = len(arr)
            i = 0
            j = 0
            while i < size:
                if arr[i] == target:
                    i += 1
                else:
                    arr[j] = arr[i]
                    i += 1
                    j += 1
            if j < len(arr):
                del arr[j:]
            return j

arr = [4, 1, 1, 2, 1, 3]
target = 3
res = Solution.solution(arr, target)
print(arr)
print(res)


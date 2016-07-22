# Remove Duplicates from Sorted Array
#
# Given a sorted array, remove the duplicates in place such that each
#  element appear atmost twice and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# Note that even though we want you to return the new length, make sure to change the original array as well in place
#
# For example,
# Given input array A = [1,1,1,2],
#
# Your function should return length = 3, and A is now [1,1,2].


class Solution:

  @staticmethod
  def solution(arr):
            size = len(arr)
            if size <= 2:
                    return size
            prev = 1
            curr = 2
            while curr < size:
                if arr[curr] == arr[prev] and arr[curr] == arr[prev - 1]:
                    curr += 1
                else:
                    prev += 1
                    arr[prev] = arr[curr]
                    curr += 1
            if prev + 1 < size:
                del arr[prev + 1:]
            return prev + 1

arr = [1, 1, 1, 2, 2, 2, 2, 3]
res = Solution.solution(arr)
print(arr)
print(res)

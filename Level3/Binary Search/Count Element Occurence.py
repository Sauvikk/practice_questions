# Given a sorted array of integers, find the number of occurrences of a given target value.
# Your algorithm’s runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return 0
#
# **Example : **
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return 2.


class Solution:

  @staticmethod
  def solution(arr, search):
        first = Solution.binarySearch(arr, search, True)
        last = Solution.binarySearch(arr, search, False)
        print(first)
        print(last)
        return last - first + 1

  @staticmethod
  def binarySearch(arr, search, searchfirst):
        low = 0
        high = len(arr)-1
        res = -1
        while low <= high:
            mid = int((low + high)/2)
            if arr[mid] == search:
                res = mid
                if searchfirst:
                    high = mid - 1
                else:
                    low = mid + 1
            elif search < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return res
arr = [5, 7, 7, 8, 8, 10]
search = 8
res = Solution.solution(arr, search)
print(res)

# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm’s runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].

# Example:
#
# Given [5, 7, 7, 8, 8, 10]
#
# and target value 8,
#
# return [3, 4].


class Solution:

   def solution(self, arr, key):
        firstindex = self.binarySearch(arr, key, True)
        lastindex = self.binarySearch(arr, key, False)
        return firstindex, lastindex

   def binarySearch(self, arr, key, searchfirst):
        low = 0
        high = len(arr)-1
        res = -1
        while low <= high:
            mid = int((low + high)/2)
            if arr[mid] == key:
                res = mid
                if searchfirst:
                    high = mid - 1
                else:
                    low = mid + 1
            elif key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return res


arr = [5, 7, 7, 8, 8, 10]
key = 8
res = Solution().solution(arr, key)
print(res)

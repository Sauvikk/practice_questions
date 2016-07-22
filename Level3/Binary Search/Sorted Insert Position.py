# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
#
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0


class Solution:

   def binarySearch(self, arr, key):
        low = 0
        high = len(arr)-1
        res = -1
        while low <= high:
            mid = int((low + high)/2)
            if arr[mid] == key:
                return mid
            elif key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        if key < arr[mid]:
            return mid
        else:
            return mid + 1

arr = [1, 3, 5, 6]
key = 0
res = Solution().binarySearch(arr, key)
print(res)
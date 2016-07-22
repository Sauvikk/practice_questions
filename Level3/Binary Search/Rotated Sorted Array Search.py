# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).
#
# You are given a target value to search. If found in the array, return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Input : [4 5 6 7 0 1 2] and target = 4
# Output : 0


class Solution:

  def binarySearch(self, arr, low, high, key):
        if low > high:
            return -1
        mid = int((low + high)/2)
        if arr[mid] == key:
            return mid
        if arr[low] <= arr[mid]:
            if key >= arr[low]  and key <= arr[mid]:
                return self.binarySearch(arr, low, mid - 1, key)
            return self.binarySearch(arr, mid + 1, high, key)

        if key >= arr[mid] and key <= arr[high]:
            return self.binarySearch(arr, mid+1, high, key)
        return self.binarySearch(arr, low, mid-1, key)

arr = [4, 5, 6, 7, 0, 1, 2]
low = 0
high = len(arr)
key = 10
res = Solution().binarySearch(arr, low, high-1, key)
print(res)


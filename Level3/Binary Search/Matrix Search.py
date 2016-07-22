# Write an efficient algorithm that searches for a value in an m x n matrix.
#
# This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
# Example:
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return 1 ( 1 corresponds to true )
#
# Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem


class Solution:

   def solution(self, arr, key):
        m = len(arr)
        n = len(arr[0])

        if not arr or len(arr) == 0 or len(arr[0]) == 0:
            return 0
        start = 0
        end = m*n-1
        while start <= end:
            mid = int((start+end)/2)
            midX = int(mid / n)
            midY = mid % n
            if arr[midX][midY] == key:
                return 1
            elif arr[midX][midY] < key:
                start = mid + 1
            else:
                end = mid - 1
        return 0


arr = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
key = 32
res = Solution().solution(arr, key)
print(res)

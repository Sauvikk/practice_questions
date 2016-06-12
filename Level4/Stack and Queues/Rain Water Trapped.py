# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.#
# Example :
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
# http://www.geeksforgeeks.org/trapping-rain-water/


class Solution:

  @staticmethod
  def solution(arr):
        n = len(arr)
        left = [0]*n
        right = [0]*n
        left[0] = arr[0]
        right[-1] = arr[-1]

        for i in range(1, n):
            left[i] = max(left[i-1], arr[i])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], arr[i])
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - arr[i]
        return water

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = Solution.solution(arr)
print(res)

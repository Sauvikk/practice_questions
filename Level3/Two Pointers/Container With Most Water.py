# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# 'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
#
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Your program should return an integer which corresponds to the maximum area of water that can be contained
# (Yes,we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with
#  for simplicity).
#
#  Note: You may not slant the container.
# Example :
#
# Input : [1, 5, 4, 3]
# Output : 6
#
# Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3.
# So total area = 3 * 2 = 6


class Solution:

  @staticmethod
  def solution(arr):
            maximum = 0
            left = 0
            right = len(arr) - 1
            while left < right:
                maximum = max(maximum, (right - left) * min(arr[left], arr[right]))
                if arr[left] < arr[right]:
                    left += 1
                else:
                    right -= 1
            return maximum

arr = [1, 5, 4, 3]
res = Solution.solution(arr)
print(res)


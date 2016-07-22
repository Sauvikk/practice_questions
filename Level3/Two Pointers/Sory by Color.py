# Given an array with n objects colored red, white or blue,
# sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: Using library sort function is not allowed.
#
# Example :
#
# Input : [0 1 2 0 1 2]
# Modify array so that it becomes : [0 0 1 1 2 2]
# http://www.programcreek.com/2014/06/leetcode-sort-colors-java/


class Solution:

  @staticmethod
  def solution(arr):
            countArray = [0] * 3
            for i in range(len(arr)):
                countArray[arr[i]] += 1
            j = 0
            k = 0
            while j < len(countArray):
                if countArray[j] != 0:
                    arr[k] = j
                    k += 1
                    countArray[j] -= 1
                else:
                    j += 1
            return arr

arr = [0, 1, 2, 0, 1, 2]
res = Solution.solution(arr)
print(res)

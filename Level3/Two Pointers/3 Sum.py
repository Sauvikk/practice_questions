# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# Example:
# given array S = {-1 2 1 -4},
# and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
# http://www.programcreek.com/2013/02/leetcode-3sum-closest-java/


class Solution:

  @staticmethod
  def solution(arr, target):
            arr.sort()
            min = 2**31 - 1
            for i in range(len(arr)):
                j = i + 1
                k = len(arr) - 1
                while j < k:
                    sum = arr[i] + arr[j] + arr[k]
                    diff = abs(sum - target)
                    if diff == 0:
                        return sum
                    elif diff < min:
                        min = diff
                        result = sum
                    elif sum < target:
                        j += 1
                    else:
                        k -= 1
            return result

arr = [3, -1, 3, 0, 0]
target = 5
res = Solution.solution(arr, target)
print(res)

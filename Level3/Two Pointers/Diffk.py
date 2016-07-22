# Given an array ‘A’ of sorted integers and another non negative integer k,
# find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
#
#  Example: Input :
#     A : [1 3 5]
#     k : 4
#  Output : YES as 5 - 1 = 4
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# Try doing this in less than linear space complexity.


class Solution:

  @staticmethod
  def solution(arr, target):
            size = len(arr)
            i, j = 0, 1
            while i < size and j < size:
                if i != j and arr[j] - arr[i] == target:
                    return 1
                elif arr[j] - arr[i] < target:
                    j += 1
                else:
                    i += 1
            return 0

arr = [1, 3, 5]
target = 4
res = Solution.solution(arr, target)
print(res)


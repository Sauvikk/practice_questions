# A long array A[] is given to you. There is a sliding window of size w which is moving from
# the very left of the array to the very right. You can only see the w numbers in the window.
# Each time the sliding window moves rightwards by one position.
#
# Example :
#
# The array is [1 3 -1 -3 5 3 6 7], and w is 3.
#
# Window position	Max
#
# [1 3 -1] -3 5 3 6 7	3
# 1 [3 -1 -3] 5 3 6 7	3
# 1 3 [-1 -3 5] 3 6 7	5
# 1 3 -1 [-3 5 3] 6 7	5
# 1 3 -1 -3 [5 3 6] 7	6
# 1 3 -1 -3 5 [3 6 7]	7
# Input: A long array A[], and a window width w
# Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
# Requirement: Find a good optimal way to get B[i]
#
#  Note: If w > length of the array, return 1 element with the max of the array.

from collections import deque


class Solution:

  @staticmethod
  def solution(arr, w):
        if w > len(arr):
            return max(arr)
        q = deque()
        i = 0
        res = []
        while i < w:
            while len(q) != 0 and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
            i += 1
        while i < len(arr):
            res.append(arr[q[0]])
            while len(q) != 0 and q[0] <= i - w:
                q.popleft()
            while len(q) != 0 and arr[i] >= arr[q[-1]]:
                q.pop()
            q.append(i)
            i += 1
        res.append(arr[q[0]])
        return res


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
res = Solution.solution(arr, 2)
print(res)

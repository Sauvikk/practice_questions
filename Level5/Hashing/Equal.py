# Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D
# are integers values in the array
#
# Note:
#
# 1) Return the indices `A1 B1 C1 D1`, so that
#   A[A1] + A[B1] = A[C1] + A[D1]
#   A1 < B1, C1 < D1
#   A1 < C1, B1 != D1, B1 != C1
#
# 2) If there are more than one solutions,
#    then return the tuple of values which are lexicographical smallest.
#
# Assume we have two solutions
# S1 : A1 B1 C1 D1 ( these are values of indices int the array )
# S2 : A2 B2 C2 D2
#
# S1 is lexicographically smaller than S2 iff
#   A1 < A2 OR
#   A1 = A2 AND B1 < B2 OR
#   A1 = A2 AND B1 = B2 AND C1 < C2 OR
#   A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
# Example:
#
# Input: [3, 4, 7, 1, 2, 9, 8]
# Output: [0, 2, 3, 5] (O index)
# If no solution is possible, return an empty list.


class Solution:

  @staticmethod
  def solution(num):
        map = {}
        result = []
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                sum = num[i] + num[j]
                if sum not in map:
                    map[sum] = (i, j)
                    continue
                first, second = map[sum]
                if first != i and first != j and second != i and second != j:
                    res = [first, second, i, j]
                    if len(result) == 0:
                        result = res
                    else:
                        for x in range(len(result)):
                            if result[x] < res[x]:
                                break
                            if result[x] > res[x]:
                                result = res
                                break
        return result
number = [3, 4, 7, 1, 2, 9, 8]
res1 = Solution.solution(number)
print(res1)

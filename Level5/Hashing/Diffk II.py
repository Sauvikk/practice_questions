# Given an array A of integers and another non negative integer k,
# find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
#
# Example :
#
# Input :
#
# A : [1 5 3]
# k : 2
# Output :
#
# 1
# as 3 - 1 = 2
#
# Return 0 / 1 for this problem.


class Solution:

  @staticmethod
  def solution(num, target):
        hash_map = {}
        for i in range(len(num)):
            hash_map[num[i]] = i
        for i in range(len(num)):
            if target + num[i] in hash_map and i != hash_map[target + num[i]] :
                return 1
        return 0
number1 = [77, 28, 19, 21, 67, 15, 53, 25, 82, 52, 8, 94, 50, 30, 37, 39, 9, 43, 35, 48, 82, 53, 16, 20, 13, 95, 18, 67, 77, 12, 93, 0 ]
# number1 = [34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29]
res1 = Solution.solution(number1, )
print(res1)

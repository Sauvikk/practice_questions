# Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
#
# Make sure the combinations are sorted.
#
# To elaborate,
# 1. Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
# 2. Entries should be sorted within themselves.
#
# Example :
# If n = 4 and k = 2, a solution is:
#
# [
#   [1,2],
#   [1,3],
#   [1,4],
#   [2,3],
#   [2,4],
#   [3,4],
# ]


class Solution:

  def dfs(self, numbers, start, k, temp, result):
        if len(temp) == k:
            result.append([x for x in temp])
            return
        for i in range(start, len(numbers)):
            temp.append(numbers[i])
            self.dfs(numbers, i + 1, k, temp, result)
            temp.pop()

  def solution(self, n, k):
        result = []
        if n <= 0 or n < k:
            return
        temp = []
        numbers = []
        for i in range(1, n+1):
            numbers.append(i)
        self.dfs(numbers, 0, k, temp, result)
        return result

res1 = Solution().solution(3, 2)
print(res1)

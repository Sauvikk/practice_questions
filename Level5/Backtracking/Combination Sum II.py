# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
#  Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# Example :
#
# Given candidate set 10,1,2,7,6,1,5 and target 8,
#
# A solution set is:
#
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]


class Solution:

  def dfs(self, numbers, start, target, temp, result):
        if target == 0:
            # for unique solution
            if temp not in result:
                result.append(temp[:])
            return
        for i in range(start, len(numbers)):
            if numbers[i] > target:
                return
            temp.append(numbers[i])
            self.dfs(numbers, i+1, target-numbers[i], temp, result)
            temp.pop()

  def solution(self, numbers, target):
        result = []
        if not numbers or len(numbers) == 0:
            return result
        temp = []
        numbers.sort()
        self.dfs(numbers, 0, target, temp, result)
        return result

res1 = Solution().solution([10, 1, 2, 7, 6, 1, 5], 8)
print(res1)
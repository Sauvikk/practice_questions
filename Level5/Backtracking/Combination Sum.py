# Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
#  Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The combinations themselves must be sorted in ascending order.
# CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR
# (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
# The solution set must not contain duplicate combinations.
# Example,
# Given candidate set 2,3,6,7 and target 7,
# A solution set is:
#
# [2, 2, 3]
# [7]
#  Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
# Example : itertools.combinations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points.


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
            self.dfs(numbers, i, target-numbers[i], temp, result)
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

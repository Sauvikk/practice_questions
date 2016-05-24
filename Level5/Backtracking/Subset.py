# Given a set of distinct integers, S, return all possible subsets.
#
#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.

from operator import itemgetter


class Solution:

  def permute(self, numbers, pos, temp, result):
        if pos == len(numbers):
            result.append(temp[:])
            return
        self.permute(numbers, pos + 1, temp, result)
        temp.append(numbers[pos])
        self.permute(numbers, pos + 1, temp, result)
        temp.pop()

  def solution(self, numbers):
        result = []
        if not numbers or len(numbers) == 0:
            return [[]]
        numbers.sort()
        temp = []
        self.permute(numbers, 0, temp, result)
        return sorted(result)

  # def solution(self, s):
  #       s.sort()
  #       r = [[]]
  #       for e in s:
  #           r += [x + [e] for x in r]
  #       return sorted(r)


res1 = Solution().solution([])
print(res1)

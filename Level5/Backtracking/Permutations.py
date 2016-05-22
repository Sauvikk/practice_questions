# Given a collection of numbers, return all possible permutations.
#
# Example:
#
# [1,2,3] will have the following permutations:
#
# [1,2,3]
# [1,3,2]
# [2,1,3]
# [2,3,1]
# [3,1,2]
# [3,2,1]
#  NOTE
# No two entries in the permutation sequence should be the same.
# For the purpose of this problem, assume that all the numbers in the collection are unique.


class Solution:

  def permute(self, numbers, start, result):
        if start == len(numbers):
            result.append([x for x in numbers])
            return
        for i in range(start, len(numbers)):
            numbers[start], numbers[i] = numbers[i], numbers[start]
            self.permute(numbers, start + 1, result)
            numbers[start], numbers[i] = numbers[i], numbers[start]

  def solution(self, numbers):
        result = []
        if not numbers or len(numbers) == 0:
            return numbers
        self.permute(numbers, 0, result)
        return result

res1 = Solution().solution([1, 2, 3])
print(res1)

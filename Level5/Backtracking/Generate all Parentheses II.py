# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
# Make sure the returned list of strings are sorted.


class Solution:

  def generate(self, result, temp, left, right):
        if left > right:
            return
        if left == 0 and right == 0:
            result.append(temp)
        if left > 0:
            self.generate(result, temp+'(', left-1, right)
        if right > 0:
            self.generate(result, temp+')', left, right-1)

  def solution(self, n):
        result = []
        if n == 0:
            return result
        temp = ""
        self.generate(result, temp, n, n)
        return sorted(result)


res1 = Solution().solution(3)
print(res1)

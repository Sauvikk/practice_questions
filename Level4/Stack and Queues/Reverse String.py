# Given a string S, reverse the string using stack.
#
# Example :
#
# Input : "abc"
# Return "cba"


class Solution:

  @staticmethod
  def solution(s):
        res = []
        for i in range(len(s)):
            res.append(s[i])
        str = ""
        for i in range(len(s)):
            str += res.pop()
        return str

s = ""
res = Solution.solution(s)
print(res)

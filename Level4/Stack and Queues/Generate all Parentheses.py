# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


class Solution:

  @staticmethod
  def solution(s):
            res = []
            for i in range(len(s)):
                if s[i] == '(' or s[i] == '[' or s[i] == '{':
                    res.append(s[i])
                elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                    if len(res) == 0:
                        return 0
                    elif (res[-1] == '(' and s[i] == ')') or (res[-1] == '{' and s[i] == '}') \
                            or (res[-1] == '[' and s[i] == ']'):
                        res.pop()
                    else:
                        return 0
            if len(res) == 0:
                return 1
            else:
                return 0

s = "[("
res = Solution.solution(s)
print(res)

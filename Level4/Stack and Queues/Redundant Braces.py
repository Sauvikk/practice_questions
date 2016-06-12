# Write a program to validate if the input string has redundant braces?
# Return 0/1
#  0 -> NO 1 -> YES
#
# Input will be always a valid expression
#
# and operators allowed are only + , * , - , /
#
# Example:
#
# ((a+b)) has redundant braces so answer will be 1
# (a + (a + b)) doesn't have have any redundant braces so answer will be 0


class Solution:

  @staticmethod
  def solution(string):
        stack = []
        for char in string:
            if char == ')':
                noChar = 0
                temp = stack.pop()
                while temp != '(':
                    noChar += 1
                    temp = stack.pop()
                print(stack)
                if noChar <= 1:
                    return 1
            else:
                stack.append(char)
        return 0


string = "((a+b)+(a+b))"
res = Solution.solution(string)
print(res)

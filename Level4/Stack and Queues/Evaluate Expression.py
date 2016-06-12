# Evaluate Expression
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Examples:
#
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class Solution:

  @staticmethod
  def solution(tokens):
        l=[]
        for str in tokens:
            if str in ["+", "-", "*", "/"]:
                a = l.pop()
                b = l.pop()
                if str == "+":
                    l.append(b+a)
                if str == "-":
                    l.append(b-a)
                if str=="*":
                    l.append(b*a)
                if str == "/":
                    l.append(int(b/(a*1.0)))
            else:
                l.append(int(str))
        return l[0]

s = "23-"
res = Solution.solution(s)
print(res)

# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
#  Note: The numbers can be arbitrarily large and are non-negative.
# Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.
# For example,
# given strings "12", "10", your answer should be “120”.
#
# NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
# We will retroactively disqualify such submissions and the submissions will incur penalties.
# http://www.programcreek.com/2014/05/leetcode-multiply-strings-java/


class Solution:

  @staticmethod
  def solution(num1, num2):
        n1 = num1[::-1]
        n2 = num2[::-1]
        n3 = [0] * (len(n1) + len(n2))
        for i in range(len(n1)):
            for j in range(len(n2)):
                n3[i+j] += int(n1[i]) * int(n2[j])
        res = []
        for i in range(len(n3)):
            mod = n3[i] % 10
            carry = int(n3[i] / 10)
            if i+1 < len(n3):
                n3[i+1] += carry
            res.insert(0, mod)
        while res[0] == 0 and len(res) > 1:
            del res[0]
        return ''.join(str(x) for x in res)

num1 = "4865486512"
num2 = "6479846542"
res = Solution.solution(num1, num2)
print(res)

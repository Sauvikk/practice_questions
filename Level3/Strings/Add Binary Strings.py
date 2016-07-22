# Given two binary strings, return their sum (also a binary string).
#
# Example:
#
# a = "100"
#
# b = "11"
# Return a + b = “111”.
# http://yucoding.blogspot.in/2012/12/leetcode-question-4-add-binary.html


class Solution:

  @staticmethod
  def solution(a, b):
            res = list(a) if len(a) > len(b) else list(b)
            str = list(b) if len(a) > len(b) else list(a)
            carry = False
            i = len(str) - 1
            j = len(res) - 1
            while i >= 0:
                if res[j] == '1' and str[i] == '1':
                    res[j] = '1' if carry else '0'
                    carry = True
                    i -= 1
                    j -= 1
                    continue
                if res[j] == '0' and str[i] == '0':
                    res[j] = '1' if carry else '0'
                    carry = False
                    i -= 1
                    j -= 1
                    continue
                if res[j] == '0' and str[i] == '1':
                    res[j] = '0' if carry else '1'
                    i -= 1
                    j -= 1
                    continue
                if res[j] == '1' and str[i] == '0':
                    res[j] = '0' if carry else '1'
                    i -= 1
                    j -= 1
                    continue
            while j >= 0 and carry:
                if res[j] == '1':
                    res[j] = '0'
                    j -= 1
                    continue
                if res[j] == '0':
                    res[j] = '1'
                    break

            if j < 0 and carry:
                res.insert(0, '1')

            return ''.join(res)

a = "111"
b = "101"
res = Solution.solution(a, b)
print(res)

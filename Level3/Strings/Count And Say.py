# The count-and-say sequence is the sequence of integers beginning as follows:
#
# 1, 11, 21, 1211, 111221, ...
# 1 is read off as one 1 or 11.
# 11 is read off as two 1s or 21.
#
# 21 is read off as one 2, then one 1 or 1211.
#
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
#
# Example:
#
# if n = 2,
# the sequence is 11.


class Solution:

  @staticmethod
  def solution(n):
        if n <= 0:
            return ""
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        string = "11"
        for i in range(3, n+1):
            count = 1
            temp = ""
            for j in range(1, len(string)):
                if string[j] != string[j-1]:
                    temp += str(count)
                    temp += string[j-1]
                    count = 1
                else:
                    count += 1
            # the above code process the previous character in the current loop, processing the last character below
            temp += str(count)
            temp += string[-1]
            string = temp
        return string

n = 10
res = Solution.solution(n)
print(res)


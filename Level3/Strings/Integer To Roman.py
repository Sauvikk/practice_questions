# Please Note:
#
# Another question which belongs to the category of questions which are intentionally stated vaguely.
# Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.
#
# Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version
#
# Input is guaranteed to be within the range from 1 to 3999.
#
# Example :
#
# Input : 5
# Return : "V"
#
# Input : 14
# Return : "XIV"
# Note : This question has a lot of scope of clarification from the interviewer.
# Please take a moment to think of all the needed clarifications and see the expected response using
# “See Expected Output” For the purpose of this question, https://projecteuler.net/about=roman_numerals
# has very detailed explanations.


class Solution:

  @staticmethod
  def solution(n):
         digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                   (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                   (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
         result = ""
         while len(digits) > 0:
            (val, roman) = digits[0] # Unpacks the first pair in the list
            if n < val:
                digits.pop(0) # Removes first element
            else:
                n -= val
                result += roman
         return result

n = 29
res = Solution.solution(n)
print(res)

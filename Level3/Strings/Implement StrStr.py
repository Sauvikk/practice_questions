# Please Note:
#
# Another question which belongs to the category of questions which are intentionally stated vaguely.
# Expectation is that you will ask for correct clarification or you will state your assumptions before you start coding.
#
# Implement strStr().
#
#  strstr - locate a substring ( needle ) in a string ( haystack ).
# Try not to use standard library string functions for this question.
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#  NOTE: Good clarification questions:
# What should be the return value if the needle is empty?
# What if both haystack and needle are empty?
# For the purpose of this problem, assume that the return value should be -1 in both cases.


class Solution:

  @staticmethod
  def solution(needle, haystack):
            if not haystack or not needle:
                return -1
            sneedle = len(needle)
            shaystack = len(haystack)
            j = 0
            while shaystack - j >= sneedle:
                begin = j
                i = 0
                while i < sneedle and j < shaystack and needle[i] == haystack[j]:
                    i += 1
                    j += 1
                if i == sneedle:
                    return begin
                j = begin + 1
            return -1

haystack = "ABCDDDEF"
needle = "DEF"
res = Solution.solution(needle,haystack )
print(res)

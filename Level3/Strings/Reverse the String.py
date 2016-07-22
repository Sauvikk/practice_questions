# Given an input string, reverse the string word by word.
#
# Example:
#
# Given s = "the sky is blue",
#
# return "blue is sky the".
#
# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.


class Solution:

  @staticmethod
  def solution(sentence):
        if not sentence or len(sentence) == 0:
            return ""
        words = sentence.split(' ')
        res = ""
        for i in range(len(words)-1, -1, -1):
            if words[i] != '':
                res += words[i] + ' '
        return "" if len(res) == 0 else res[0: len(res)-1]

sentence = "j"
res = Solution.solution(sentence)
print(res)

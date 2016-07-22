# Write a function to find the longest common prefix string amongst an array of strings.
#
# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
#
# As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
#
# Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.
#
# Example:
#
# Given the array as:
#
# [
#
#   "abcdefgh",
#
#   "aefghijk",
#
#   "abcefgh"
# ]
# The answer would be “a”.


class Solution:

  @staticmethod
  def solution(sentences):
        if not sentences or len(sentences) == 0:
            return ""
        minLen = len(sentences[0])
        for s in sentences:
            if len(s) < minLen:
                minLen = len(s)

        for j in range(minLen):
            prev = '0'
            for i in range(len(sentences)):
                if i == 0:
                    prev = sentences[i][j]
                    continue
                if sentences[i][j] != prev:
                    return sentences[i][0: j]
        return sentences[0][0: minLen]

sentences = ["abcdefgh",  "abcefgh"]
res = Solution.solution(sentences)
print(res)

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Example:
#
# "A man, a plan, a canal: Panama" is a palindrome.
#
# "race a car" is not a palindrome.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


class Solution:

  @staticmethod
  def solution(sentence):
        if not sentence or len(sentence) == 0:
            return 1
        start = 0
        end = len(sentence) - 1
        while start < end:
            if not sentence[start].isalnum():
                start += 1
                continue
            if not sentence[end].isalnum():
                end -= 1
                continue
            if sentence[start].lower() != sentence[end].lower():
                return 0
            else:
                start += 1
                end -= 1
        return 1

sentence = "A man, a plan, a canal: Panama"
res = Solution.solution(sentence)
print(res)

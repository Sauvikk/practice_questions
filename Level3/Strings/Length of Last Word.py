# Given a string s consists of upper/lower-case alphabets and
# empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Given s = "Hello World",
#
# return 5 as length("World") = 5.
#
# Please make sure you try to solve this problem without using library functions.
# Make sure you only traverse the string once.


class Solution:


  # @staticmethod
  # def solution(string):
  #       count = 0
  #       if not string or len(string) == 0:
  #           return count
  #       flag = False
  #       for i in range(len(string)-1, -1, -1):
  #           c = string[i]
  #           if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
  #               flag = True
  #               count += 1
  #           else:
  #               if flag:
  #                   return count
  #       return count

  # A word is defined as a character sequence consists of non-space characters only.
  @staticmethod
  def solution(string):
        count = 0
        if not string or len(string) == 0:
            return count
        for i in range(len(string)-1, -1, -1):
            c = string[i]
            if c != ' ':
                count += 1
            else:
                if count > 0:
                    return count
        return count

string = "Wordl   "
res = Solution.solution(string)
print(res)

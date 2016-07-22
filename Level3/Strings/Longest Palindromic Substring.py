# Given a string S, find the longest palindromic substring in S.
#
# Substring of string S:
#
# S[i...j] where 0 <= i <= j < len(S)
#
# Palindrome string:
#
# A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.
#
# Incase of conflict, return the substring which occurs first ( with the least starting index ).
#
# Example :
#
# Input : "aaaabaaa"
# Output : "aaabaaa"


class Solution:

  @staticmethod
  def solution(s):
            if not s:
                return None
            if len(s) <= 1:
                return s
            maxlen = 1
            longeststr = []
            flag = True
            length = len(s)
            table = [[0 for x in range(length)] for y in range(length)]
            for i in range(length):
                table[i][i] = 1
            start = 0
            for i in range(length - 1):
                if s[i] == s[i + 1]:
                    table[i][i + 1] = 1
                    if flag:
                        start = i
                        maxlen = 2
                        flag = False
            for k in range(3, length + 1):
                for i in range(length - k + 1):
                    j = i + k - 1
                    if s[i] == s[j] and table[i+1][j-1]:
                        table[i][j] = 1
                        if k > maxlen:
                            start = i
                            maxlen = k
            return s[start: start + maxlen]

string = "abcdddef"
res = Solution.solution(string)
print(res)

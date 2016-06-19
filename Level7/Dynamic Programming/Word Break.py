# Given a string s and a dictionary of words dict, determine if s can be segmented into a
# space-separated sequence of one or more dictionary words.
#
# For example, given
#
# s = "myinterviewtrainer",
# dict = ["trainer", "my", "interview"].
# Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
# http://www.programcreek.com/2012/12/leetcode-solution-word-break/


class Solution:
    def sol(self, s, dic):
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for string in dic:
                end = i + len(string)
                if end > len(s):
                    continue
                if dp[end]:
                    continue
                if s[i: end] == string:
                    dp[end] = True
        return dp[len(s)]


s1 = "myinterviewtrainer"
dict1 = ["trainer", "my", "interview"]
print(Solution().sol(s1, dict1))

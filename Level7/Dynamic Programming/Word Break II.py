# Given a string s and a dictionary of words dict,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
#
# Return all such possible sentences.
#
# For example, given
#
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# A solution is
#  [ "cats and dog", "cat sand dog" ]
#
# Make sure the strings are sorted in your result.
# http://buttercola.blogspot.in/2014/08/leetcode-word-break-ii.html
# http://www.programcreek.com/2014/03/leetcode-word-break-ii-java/


class Solution:
    def sol(self, s, dic):
        dp = [None] * (len(s) + 1)
        dp[0] = []
        for i in range(len(s)):
            if dp[i] is None:
                continue
            for string in dic:
                end = i + len(string)
                if end > len(s):
                    continue
                if s[i: end] == string:
                    if dp[end] is None:
                        dp[end] = []
                    if string in dp[end]:
                        continue
                    dp[end].append(string)
        result = []
        if dp[len(s)] is None:
            return result
        temp = []
        self.dfs(dp, result, "", len(s))
        return sorted(result)

    def dfs(self, pos, result, curr, i):
        if i == 0:
            result.append(curr.strip())
            return
        for s in pos[i]:
            combined = s + " " + curr
            self.dfs(pos, result, combined, i - len(s))


s1 = "catsanddog"
dict1 = ["cat", "cats", "and", "sand", "dog"]
print(Solution().sol(s1, dict1))

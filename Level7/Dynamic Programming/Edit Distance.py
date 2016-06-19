# Given two words A and B, find the minimum number of
# steps required to convert A to B. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example :
# edit distance between
# "Anshuman" and "Antihuman" is 2.
#
# Operation 1: Replace s with t.
# Operation 2: Insert i.


class Solution:

    def dp(self, s1, s2, m, n):
        dp = [[0 for x in range(n+1)] for x in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[m][n]

    def sol(self, s1, s2):
        ans = self.dp(s1, s2, len(s1), len(s2))
        return ans


x = "Anshuman"
y = "Antihuman"
print(Solution().sol(x, y))

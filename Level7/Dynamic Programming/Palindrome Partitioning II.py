# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example :
# Given
# s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


class Solution:
    def sol(self, s):
        n = len(s)
        count = [0] * n
        dp = [[0 for x in range(n)] for x in range(n)]
        for i in range(n):
            dp[i][i] = True
        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i + l - 1
                if l == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
        for i in range(0, n):
            if dp[0][i] is True:
                count[i] = 0
            else:
                count[i] = 2**31 - 1
                for j in range(i):
                    if dp[j+1][i] is True and 1 + count[j] < count[i]:
                        count[i] = 1 + count[j]
        return count[n-1]

print(Solution().sol("ababb"))

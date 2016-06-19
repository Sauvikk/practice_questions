# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# Example :
#
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.


class Solution:

    def is_valid(self, s):
        if s[0] == '0':
            return False
        value = int(s)
        return value >= 1 and value <= 26

    def sol(self, string):
        if string is None or len(string) == 0 or string == '0':
            return 0
        dp = [0] * (len(string)+1)
        dp[0] = 1
        if self.is_valid(string[0: 1]):
            dp[1] = 1
        else:
            dp[1] = 0
        for i in range(2, len(string)+1):
            if self.is_valid(string[i-1: i]):
                dp[i] += dp[i-1]
            if self.is_valid(string[i-2: i]):
                dp[i] += dp[i-2]
        return dp[len(string)]


print(Solution().sol("00"))

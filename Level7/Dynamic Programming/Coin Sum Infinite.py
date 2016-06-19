# You are given a set of coins S. In how many ways can you make sum
# N assuming you have infinite amount of each coin in the set.
#
# Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).
#
# Example :
#
# Input :
# 	S = [1, 2, 3]
# 	N = 4
#
# Return : 4
#
# Explanation : The 4 possible ways are
# {1, 1, 1, 1}
# {1, 1, 2}
# {2, 2}
# {1, 3}
# Note that the answer can overflow. So, give us the answer % 1000007


class Solution:
    # @param n, an integer
    # @return an integer
    def coin_sum(self, s, len_s, target):
        table = [0]*(target+1)
        table[0] = 1
        for i in range(len_s):
            for j in range(s[i], target+1):
                table[j] += table[j-s[i]]
        return table[target] % 1000007


c = [2, 5, 3, 6]
print(Solution().coin_sum(c, len(c), 10))

# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# Return an integer corresponding to the maximum product possible.
#
# Example :
#
# Input : [2, 3, -2, 4]
# Return : 6
#
# Possible with [2, 3]
# http://yucoding.blogspot.in/2014/10/leetcode-quesion-maximum-product.html


class Solution:
    # @param n, an integer
    # @return an integer
    def sol(self, num):
        maximum = [None] * len(num)
        minimum = [None] * len(num)
        maximum[0] = minimum[0] = result = num[0]
        for i in range(1, len(num)):
            if num[i] > 0:
                maximum[i] = max(num[i], maximum[i-1]*num[i])
                minimum[i] = min(num[i], minimum[i-1]*num[i])
            else:
                maximum[i] = max(num[i], minimum[i-1]*num[i])
                minimum[i] = min(num[i], maximum[i-1]*num[i])
            result = max(result, maximum[i])
        return result

c = [2, 3, -2, 4]
print(Solution().sol(c))


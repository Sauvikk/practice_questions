# There are N children standing in a line. Each child is assigned a rating value.
#
#  You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Sample Input :
#
# Ratings : [1 2]
# Sample Output :
#
# 3
# The candidate with 1 rating gets 1 candy and candidate with rating cannot get 1 candy as 1 is
# its neighbor. So rating 2 candidate gets 2 candies. In total, 2+1 = 3 candies need to be given out.


class Solution:
    def sol(self, rating):
        if rating is None or len(rating) == 0:
            return 0
        candies = [0] * len(rating)
        candies[0] = 1
        for i in range(1, len(candies)):
            if rating[i] > rating[i - 1]:
                candies[i] = candies[i - 1] + 1
            else:
                candies[i] = 1
        result = candies[-1]
        for i in range(len(candies) - 2, -1, -1):
            if rating[i] > rating[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            result += candies[i]
        return result


res1 = Solution().sol([1, 2])
print(res1)

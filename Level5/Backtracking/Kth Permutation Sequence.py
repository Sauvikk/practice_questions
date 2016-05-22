# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3 ) :
#
# 1. "123"
# 2. "132"
# 3. "213"
# 4. "231"
# 5. "312"
# 6. "321"
# Given n and k, return the kth permutation sequence.
#
# For example, given n = 3, k = 4, ans = "231"
#
#  Good questions to ask the interviewer :
# What if n is greater than 10. How should multiple digit numbers be represented in string?
# > In this case, just concatenate the number to the answer.
# > so if n = 11, k = 1, ans = "1234567891011"
# Whats the maximum value of n and k?
# > In this case, k will be a positive integer thats less than INT_MAX.
# > n is reasonable enough to make sure the answer does not bloat up a lot.
# http://stackoverflow.com/questions/31216097/given-n-and-k-return-the-kth-permutation-sequence


class Solution:

  def solution(self, n, k):
        k -= 1
        numbers = [0]*n
        indices = [0]*n
        for i in range(n):
            numbers[i] = i+1
        divisor = 1
        for place in range(1, n+1):
            if int(k/divisor) == 0:
                break
            indices[n-place] = int(k/divisor) % place
            divisor *= place

        for i in range(n):
            index = indices[i] + i
            if index != i:
                temp = numbers[index]
                j = index
                while j > i:
                    numbers[j] = numbers[j-1]
                    j -= 1
                numbers[i] = temp
        return ''.join(str(x) for x in numbers)

res1 = Solution().solution(3, 6)
print(res1)

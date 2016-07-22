# Given an array with non negative numbers, divide the array into two parts
# such that the average of both the parts is equal.
# Return both parts (If exist).
# If there is no solution. return an empty list.
#
# Example:
#
#
# Input:
# [1 7 15 29 11 9]
#
# Output:
# [9 15] [1 7 11 29]
#
# The average of part is (15+9)/2 = 12,
# average of second part elements is (1 + 7 + 11 + 29) / 4 = 12
#
#  NOTE 1: If a solution exists, you should return a list of exactly 2 lists of
# integers A and B which follow the following condition :
# * numElements in A <= numElements in B
# * If numElements in A = numElements in B, then A is lexicographically
# smaller than B ( https://en.wikipedia.org/wiki/Lexicographical_order )
# NOTE 2: If multiple solutions exist, return the solution where length(A) is minimum.
# If there is still a tie, return the one where A is lexicographically smallest.
# NOTE 3: Array will contain only non negative numbers.


class Solution:

    def __init__(self):
        self.res = []
        self.dp = []
        self.real = []
        self.total = 0

    def is_possible(self, index, sum_m, length):
        if length == 0:
            return True if sum_m == 0 else False
        if index >= self.total:
            return False
        if self.dp[index][sum_m][length] is False:
            return False
        if sum_m >= self.real[index]:
            self.res.append(self.real[index])
            if self.is_possible(index+1, sum_m-self.real[index], length-1):
                return True
            self.res.pop()
        if self.is_possible(index+1, sum_m, length):
            return True
        self.dp[index][sum_m][length] = False
        return self.dp[index][sum_m][length]

    def sol(self, arr):
        arr.sort()
        self.real = arr
        total_sum = sum(arr)
        self.total = len(arr)
        self.dp = [[[True for x in range(0, self.total)]for x in range(0, total_sum+1)]for x in range(0, len(self.real))]

        for i in range(1, self.total):
            if ((total_sum*i) % self.total) != 0:
                continue
            sum_of_set1 = int((total_sum * i) / self.total)
            if self.is_possible(0, sum_of_set1, i):
                ptr1 = 0
                ptr2 = 0
                res1 = self.res
                res2 = []
                while ptr1 < len(arr) or ptr2 < len(self.res):
                    if ptr2 < len(self.res) and self.res[ptr2] == arr[ptr1]:
                        ptr1 += 1
                        ptr2 += 1
                        continue
                    res2.append(arr[ptr1])
                    ptr1 += 1
                ans = [res1, res2]
                return ans
        return []

c = [1, 7, 15, 29, 11, 9]
print(Solution().sol(c))


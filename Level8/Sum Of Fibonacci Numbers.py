# How many minimum numbers from fibonacci series are
# required such that sum of numbers should be equal to a given Number N?
# Note : repetition of number is allowed.
#
# Example:
#
# N = 4
# Fibonacci numbers : 1 1 2 3 5 .... so on
# here 2 + 2 = 4
# so minimum numbers will be 2


class Solution:
    def sol(self, n):

        if n < 2:
            return 2
        a = 1
        b = 1
        fib_sum = [1, 1]
        while True:
            c = a + b
            if c <= n:
                fib_sum.append(c)
            else:
                break
            a = b
            b = c
        count = 0
        index = len(fib_sum) - 1
        while n > 0:
            fib = fib_sum[index]
            if n >= fib:
                count += int(n/fib)
                n %= fib
            index -= 1
        return count

print(Solution().sol(4))

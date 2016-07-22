# Given N and M find all stepping numbers in range N to M
#
# The stepping number:
#
# A number is called as a stepping number if the adjacent digits have a difference of 1.
# e.g 123 is stepping number, but 358 is not a stepping number
#
# Example:
#
# N = 10, M = 20
# all stepping numbers are 10 , 12
# Return the numbers in sorted order.

from collections import deque


class Solution:
    def edges(self, n):
        ret = []
        if n == 0:
            return range(1, 10)
        else:
            temp = n % 10
            temp1 = n * 10 + temp
            if temp == 0:
                return [temp1 + 1]
            elif temp == 9:
                return [temp1 - 1]
            else:
                return [temp1 - 1, temp1 + 1]

    def sol(self, A, B):
        if A > B:
            A, B = B, A
        ret = []
        if A <= 0:
            ret.append(0)
        Q = deque()
        Q.append(0)
        while len(Q) != 0:
            curr = Q.popleft()
            for i in self.edges(curr):
                Q.append(i)
                if i > B:
                    Q = deque()
                    break
                else:
                    if i < A:
                        continue
                    elif i >= A and i <= B:
                        ret.append(i)
        return ret

print(Solution().sol(10, 20))

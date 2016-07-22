# Knight movement on a chess board
#
# Given any source point and destination point on a chess board,
# we need to find whether Knight can move to the destination or not.
#
# Knight's movements
#
# The above figure details the movements for a knight
# ( 8 possibilities ). Note that a knight cannot go out of the board.
#
# If yes, then what would be the minimum number of steps for the knight to move to the said point.
# If knight can not move from the source point to the destination point, then return -1
#
# Input:
#
# N, M, x1, y1, x2, y2
# where N and M are size of chess board
# x1, y1  coordinates of source point
# x2, y2  coordinates of destination point
# Output:
#
# return Minimum moves or -1
# Example
#
# Input : 8 8 1 1 8 8
# Output :  6

from collections import deque


class Solution:
    def __init__(self):
        self.dx = [2, 2, -2, -2, 1, 1, -1, -1]
        self.dy = [-1, 1, 1, -1, 2, -2, 2, -2]

    def valid(self, x, y, n, m):
        if x <= 0 or y <= 0 or x > n or y > m:
            return False
        return True

    def bfs(self, p1, p2, p3):
        n = p3[0]
        m = p3[1]
        q = deque()
        vis = {}
        q.append((p1, 0))
        while len(q) != 0:
            temp = q[0]
            q.popleft()
            if temp[0][0] == p2[0] and temp[0][1] == p2[1]:
                return temp[1]
            x = temp[0][0]
            y = temp[0][1]
            dis = temp[1] + 1
            if (x, y) in vis:
                continue
            vis[(x, y)] = True
            for i in range(8):
                x1 = x + self.dx[i]
                y1 = y + self.dy[i]
                if self.valid(x1, y1, n, m):
                    q.append(((x1, y1), dis))
        return -1

    def knight(self, n, m, x1, y1, x2, y2):
        p1 = (x1, y1)
        p2 = (x2, y2)
        p3 = (n, m)
        ans = self.bfs(p1, p2, p3)
        return ans


print(Solution().knight(2, 20, 1, 18, 1, 5))

# You are given with an array of 1s and 0s. And you are given with an integer M,
#  which signifies number of flips allowed.
# Find the position of zeros which when flipped will produce maximum continuous series of 1s.
#
# For this problem, return the indices of maximum continuous series of 1s in order.
#
# Example:
#
# Input :
# Array = {1 1 0 1 1 0 0 1 1 1 }
# M = 1
#
# Output :
# [0, 1, 2, 3, 4]
#
# If there are multiple possible solutions, return the sequence which has the minimum start index.



class Solution:


  def solution(self, arr, m):
            maxLength = 0
            start = 0
            curZerosCnt = 0
            curStart = 0
            curLength = 0

            for i in range(len(arr)):
                if arr[i] == 0:
                    curZerosCnt += 1
                if arr[i] == 0 and curZerosCnt > m:
                    nStart = self.findLeftMostZeroInclusive(arr, curStart)
                    curLength -= nStart - curStart -1
                    print(curLength)
                    curStart = nStart
                    curZerosCnt -= 1
                    continue
                curLength += 1
                if curLength > maxLength:
                    maxLength = curLength
                    start = curStart
            for i in range(start, len(arr)):
                if arr[i] == 0 and m != 0:
                    arr[i] = 1
                    m -= 1
            res = []
            print(maxLength)
            for i in range(start, maxLength):
                if arr[i] == 0 and m != 0:
                    arr[i] = 1
                    m -= 1
                    res.append(i)
                res.append(i)
            return res

  def findLeftMostZeroInclusive(self, arr, curStart):
            i = curStart
            while arr[i] != 0 and i <= len(arr)-1:
                i += 1
            return i + 1

arr = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
res = Solution().solution(arr, 1)
print(res)
print(arr)

# There are two sorted arrays A and B of size m and n respectively.
#
# Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).
#
# The overall run time complexity should be O(log (m+n)).
#
# Sample Input
#
# A : [1 4 5]
# B : [2 3]
#
# Sample Output
# 3
# WRONG !!!


class Solution:

  def MO2(self, a, b):
        return (a + b)/2

  def MO3(self, a, b, c):
        return a + b + c - max(a, max(b, c)) - min(a, min(b, c))

  def MO4(self, a, b, c, d):
        maximum = max(a, max(b, max(c, d)))
        minimum = min(a, min(b, min(c, d)))
        return (a + b + c + d - maximum - minimum)/2

  def medianSingle(self, arr):
        n = len(arr)
        if n == 0:
                return -1
        if n % 2 == 0:
                return (arr[int(n/2)] + arr[int(n/2-1)])/2
        return arr[n/2]

  def findMedianUtil(self, A, B):
        n = len(A)
        m = len(B)
        if n == 0:
                return self.medianSingle(B)
        if n == 1:
                if m == 1:
                    return self.MO2(A[0], B[0])
                if m % 2 != 0:
                    return self.MO2(B[int(m/2)], self.MO3(A[0], B[int(m/2 - 1)], B[int(m/2 + 1)]))
                return self.MO3(B[int(m/2)], B[int(m/2 - 1)], A[0])

        elif n == 2:
                if m == 2:
                     return self.MO4(A[0], A[1], B[0], B[1])
                if m % 2 != 0:
                     return self.MO3(B[int(m/2)], max(A[0], B[int(m/2 - 1)]), min(A[1], B[int(m/2 + 1)]))
                return self.MO4(B[int(m/2)], B[int(m/2 - 1)], max(A[0], B[int(m/2 - 2)]), min(A[1], B[int(m/2 + 1)]))

        idxA = int((n -1)/2)
        idxB = int((m -1)/2)

        if A[idxA] <= B[idxB]:
                 return self.findMedianUtil(A[idxA::], B[0:idxB])

        return self.findMedianUtil(A[0: idxA], B[idxB::])

  def solution(self, A, B):

        if len(A) > len(B):
            return self.findMedianUtil(B, A)
        return self.findMedianUtil(A, B)


A = [ -50, -41, -40, -19, 5, 21, 28 ]
B = [-50, -21, -10]
print(Solution().solution(A, B))
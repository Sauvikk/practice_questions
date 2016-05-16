class SpiralOrderMatrix:

    def spiralOrder(self, A):
        result = []
        t = 0
        b = len(A)-1
        l = 0
        r = len(A[0])-1
        dir = 0

        while t <= b and l <= r:
            if dir == 0:
                for i in range(l, r+1):
                    result.append(A[t][i])
                t += 1
                dir = 1
            elif dir == 1:
                for i in range(t, b+1):
                    result.append(A[i][r])
                r -= 1
                dir = 2
            elif dir == 2:
                for i in range(r, l-1, -1):
                    result.append(A[b][i])
                    # print(A[b][i])
                b -= 1
                dir = 3
            elif dir == 3:
                for i in range(b, t-1, -1):
                    result.append(A[i][l])
                    # print(A[i][l])
                l += 1
                dir = 0
        return result

som = SpiralOrderMatrix()
myArray = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
arr = som.spiralOrder(myArray)
print(len(arr))
for i in range(len(arr)):
    print(str(arr[i]) + " ")


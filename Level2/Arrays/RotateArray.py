class RotateArray:

    def rotateArray(self, a, b):
        ret = []
        if b > len(a):
            b %= len(a)
        for i in range(b, len(a)):
            ret.append(a[i])
        for i in range(0, b):
            ret.append(a[i])
        return ret

ra = RotateArray()
a = [1, 2, 3, 4, 5, 6]
res = ra.rotateArray(a, 1)
for i in range(len(res)):
    print(str(res[i]) + " ")

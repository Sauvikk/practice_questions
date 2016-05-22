# Implement pow(A, B) % C.
#
# In other words, given A, B and C,
# find (AB)%C.
#
# Input : A = 2, B = 3, C = 3
# Return : 2
# 2^3 % 3 = 8 % 3 = 2


def mod(x, n, m):
        if m == 1:
            return 0
        if n == 0:
            return 1
        elif n % 2 == 0:
            y = mod(x, n/2, m)
            return (y*y) % m
        else:
            return ((x % m) * mod(x, n-1, m)) % m

res1 = mod(0, 0, 1)
print(res1)

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

common = []
min_multi = []

for i in range(1, min(A, B)+1):
    if A % i == 0 and B % i == 0:
        common.append(i)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

min_multi = A * B // gcd(A, B)

print(max(common))
print(min_multi)
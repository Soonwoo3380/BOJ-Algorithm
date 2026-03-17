import sys
input = sys.stdin.readline

N, K = map(int, input().split())

numerator = 1
denominator = 1

for i in range(N-K+1, N+1):
    numerator *= i

for j in range(1, K+1):
    denominator *= j

print(numerator // denominator)
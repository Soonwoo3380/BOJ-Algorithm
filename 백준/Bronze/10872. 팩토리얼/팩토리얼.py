N = int(input())

a = 1
for i in range(1, N+1):
    if N == 0:
        a *= 0
    else:
        a *= i
print(a)
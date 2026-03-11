N = int(input())

a, b = 1, 1
answer = 1

if N == 0:
    answer = 0
else:
    for _ in range(N-2):
        answer = a + b
        a, b = b, answer

print(answer)
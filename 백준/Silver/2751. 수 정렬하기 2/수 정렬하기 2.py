import sys
input = sys.stdin.readline

N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

numbers = sorted(numbers)

for num in numbers:
    print(num)

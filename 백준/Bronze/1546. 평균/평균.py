import sys
input = sys.stdin.readline

N = int(input())

input_list = list(map(int, input().split()))

M = max(input_list)

for i in range(N):
    input_list[i] = input_list[i]/M*100

print((sum(input_list)/N))
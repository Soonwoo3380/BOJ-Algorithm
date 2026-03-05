import sys
input = sys.stdin.readline

N = int(input())

size_list = list(map(int, input().split()))

T, P = map(int, input().split())


for i in range(len(size_list)):
    if size_list[i] == 0:
        size_list[i] = 0
    elif size_list[i] % T == 0:
        size_list[i] = size_list[i] // T
    else:
        size_list[i] = (size_list[i] // T) + 1


print(sum(size_list))
print(N // P, N % P)
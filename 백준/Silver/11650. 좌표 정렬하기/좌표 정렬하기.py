import sys
input = sys.stdin.readline

N = int(input())

list_arr = []

for _ in range(N):
    A, B = map(int, input().split())
    list_arr.append((A, B))

list_arr.sort(key=lambda x: (x[0], x[1]))

for A, B in list_arr:
    print(A, B)
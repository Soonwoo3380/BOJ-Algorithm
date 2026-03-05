import sys
input = sys.stdin.readline

N = int(input())
A_set = set(map(int, input().split()))
M = int(input())
B_list = list(map(int, input().split()))

for x in B_list:
    if x in A_set:
        print(1)
    else:
        print(0)
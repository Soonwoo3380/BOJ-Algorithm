import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

maximum_height = 0
low = 0
high = max(trees)
answer = 0

while low <= high:

    mid = (low+high) // 2
    logging = sum(tree-mid for tree in trees if tree > mid)

    if logging >= M:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
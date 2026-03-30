import sys
input = sys.stdin.readline

N, C = map(int, input().split())

houses = [int(input()) for _ in range(N)]

houses.sort()

right = houses[-1] - houses[0]
left = 1

result = 0

while left <= right:
    mid = (left + right) // 2
    count = 1
    last_val = houses[0]

    for i in range(1, len(houses)):
        if abs(last_val - houses[i]) >= mid:
            count += 1
            last_val = houses[i]
        else:
            pass

    if count >= C:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num_list = list(map(int, input().split()))

left = 0
right = 0
current = 0
answer = N + 1


while right <= N:
    if current >= S:
        answer = min(answer, right - left)
        current -= num_list[left]
        left += 1
    else:
        if right == N:
            break
        current += num_list[right]
        right += 1

print(0 if answer == N + 1 else answer)
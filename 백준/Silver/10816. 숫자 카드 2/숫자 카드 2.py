import sys
input = sys.stdin.readline

N = int(input())
num_cards = list(map(int, input().split()))
M = int(input())
compare_cards = list(map(int, input().split()))

count_dict = {}
for x in num_cards:
    count_dict[x] = count_dict.get(x, 0) + 1

result = [count_dict.get(num, 0) for num in compare_cards]
print(*result)
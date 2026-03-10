import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

comb_list = []

for comb in combinations(cards, 3):
    comb_list.append(sum(comb))

comb_list = sorted(comb_list)

result = []
for num in comb_list:
    if num <= M:
        result.append(num)

print(max(result))
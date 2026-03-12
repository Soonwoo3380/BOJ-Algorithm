import sys
input = sys.stdin.readline

dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

from itertools import combinations

dwarfs_7 = [comb for comb in combinations(dwarfs, 7)]
result = [sum(comb) for comb in dwarfs_7]

idx = [i for i in range(len(result)) if result[i] == 100][0]

for num in sorted(dwarfs_7[idx]):
    print(num)
import sys
input = sys.stdin.readline

N = int(input())
words_set = set()

for _ in range(N):
    words_set.add(input().strip())

words = sorted(words_set, key=lambda x: (len(x), x))

for word in words:
    print(word)
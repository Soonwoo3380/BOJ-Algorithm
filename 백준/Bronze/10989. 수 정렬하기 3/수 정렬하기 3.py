import sys

int_num = int(sys.stdin.readline())

count = [0] * 10001

for _ in range(int_num):
    num = int(sys.stdin.readline())
    count[num] += 1

for value in range(1, 10000+1):
    if count[value] > 0:
        for _ in range(count[value]):
            print(value)

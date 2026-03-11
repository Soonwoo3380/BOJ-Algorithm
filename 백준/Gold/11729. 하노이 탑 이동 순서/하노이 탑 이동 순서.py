import sys
input = sys.stdin.readline

N = int(input())

def hanoi(n, from_, dest, via):
    if n == 1:
        print(f'{from_} {dest}')
        return
    hanoi(n-1, from_, via, dest)
    print(f'{from_} {dest}')
    hanoi(n-1, via, dest, from_)
    
print((2**N)-1)
hanoi(N, 1, 3, 2)
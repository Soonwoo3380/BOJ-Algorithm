A, B, C, D, E = map(int, input().split())

last_number = (A**2+B**2+C**2+D**2+E**2) % 10

print(last_number)
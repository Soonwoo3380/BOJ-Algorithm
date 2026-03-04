n = list(range(1, 30+1))


for _ in range(28):
    input_numbers = int(input())
    n.remove(input_numbers)
    
print(min(n))
print(max(n))
    
    
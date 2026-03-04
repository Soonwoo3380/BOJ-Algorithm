N = int(input())

def factorial_addition(number):
    result = 0
    for k in range(1, number+1):
        result += k
    return result

for _ in range(N):
    answer = list(map(str, input().split('X')))
    
    filtered_answer = [item for item in answer if item != '']
       
    result = []
    for i in range(0, len(filtered_answer)):
        result.append(len(filtered_answer[i]))
        
    final_result = []
    for i in range(0, len(result)):
        final_result.append(factorial_addition(result[i]))

    print(sum(final_result))
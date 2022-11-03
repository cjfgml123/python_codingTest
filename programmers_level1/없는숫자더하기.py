def MySolution(numbers):
    answer = 0
    for i in range(1,10):
        if i not in numbers:
            answer += i
    return answer

def solution(numbers):
    return 45 - sum(numbers)
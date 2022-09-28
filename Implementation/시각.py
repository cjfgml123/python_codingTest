# 00 시 00분 00초 ~ N시 59분 59초 까지 3이 들어가 있는 경우의 수 구하기
def self_solution():
    N = int(input())

    _count = 0
    for hour in range(N+1):
        if '3' in str(hour) :
            _count += 60 * 60        
        else :
            for min in range(60):
                for sec in range(60):
                    if ('3' in str(min)) or ('3' in str(sec)):
                        _count += 1
    print(_count) 

def solution():
    h = int(input())
    
    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1 
    print(count)

solution()
# 거스름돈으로 사용할 500원, 100원, 50원, 10원 동전이 무한할 때 손님에게 거슬러줘야 할 돈이 N원일 경우
# 거슬러 줘야할 동전의 최소 개수를 구하라. N은 항상 10의 배수

def self_solution(N):
    _list = [500,100,50,10]
    _count = 0
    for i in _list:
        result = N // i 
        _count += result
        N = N % i 
    return _count
    
def solution(n):
    count = 0
    coin_types = [500,100,50,10]
    for coin in coin_types:
        count += n // coin 
        n %= coin 
    return count 

#print(self_solution(1260))    
print(solution(1260))
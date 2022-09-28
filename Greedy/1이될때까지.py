n, k = map(int,input().split())

def self_solution(n,k):
    _count = 0
    while(True):
        if n == 1 :
            break
        if n % k == 0:
            n = n / k
        else :
            n -= 1    
        _count += 1
    print(_count)

def solution(n,k):
    result = 0
    
    while True:
        target = (n//k) * k
        result += n - target
        n = target
        
        if n < k:
            break
        
        result += 1
        n //= k
    
    result += n - 1
    print(result)

solution(n,k)
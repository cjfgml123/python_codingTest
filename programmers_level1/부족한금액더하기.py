def solution(price, money, count):
    _sumVal = 0
    for i in range(1,count+1):
        _sumVal += price * i 

    if money - _sumVal > 0:
        return 0
    else:
        return abs(money - _sumVal)
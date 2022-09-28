import time
import sys 

def self_solution(_N,_M,_K,_valList:list): # N : 배열의 크기, M : 숫자가 더해지는 횟수 , K : 같은 인덱스의 숫자를 더할 수 있는 최대횟수 
    _answer = 0
    k = 1
    M = 0

    while(True):
        if M == _M:
            break
        if k <= _K:
            _answer += _valList[0]
            k += 1
            #print("a",_answer,k)
        else :
            _answer += _valList[1]
            k = 1
            #print("b",_answer,k)
        M += 1
    return _answer

# readline() : 파일의 한 줄을 가져와 문자열로 반환 , 파일 포인터는 그 다음줄로 이동
# readlines() : 파일 내용 전체를 가져와 리스트로 반환, 각 줄은 문자열 형태로 리스트의 요소로 저장
#_inputStr = sys.stdin.readline().rstrip()
#_inputVal = sys.stdin.readline().rstrip()

#_input = list(map(int,_inputStr.split()))
#_inputVal = list(map(int,_inputVal.split()))
_input = [5,8,3]
_inputVal = [2,4,5,4,6]
_inputVal.sort(reverse=True) 
print(self_solution(_input[0],_input[1],_input[2],_inputVal))

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
n, m ,k = map(int,input().split())
_data = list(map(int,input().split()))

def solution(_N,_M,_K,_data):
    _answer = 0
    _data.sort()
    _first = _data[n-1] # 첫 번째로 큰 수
    _second = _data[n-2] # 두 번째로 큰 수
    # 가장 큰 수가 더해지는 횟수 계산
    _count = (m // (k+1)) * k 
    _count += m % (k+1) # m이 (k+1)로 나누어 떨어지지 않을 때 나머지는 가장 큰 수만 남음.
    
    _answer += _count * _first
    _answer += (_M - _count) * _second
    return _answer

print(solution(n,m,k,_data))


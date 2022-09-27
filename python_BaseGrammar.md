### Python 기초 문법 

```python
# round(값 , 반올림하고자 하는 위치 -1)
_val = round(123.456,2)
print(_val)  # 123.46

# 자료형 연산
_a = 7
_b = 3

print(_a / _b) # 나누기 2.333333... 파이썬에서 나누기 연산자는 나눠진 결과를 기본적으로 실수형으로 처리
print(_a % _b) # 나머지 1
print(_a // _b) # 몫 2
print(_a ** _b) # 거듭제곱 연산
```



#### list()

```python
# 리스트 선언
_list = [1,2,3,4]
_list_1 = list() # 빈 리스트 선언 

# 크기가 N이고 모든 값이 0인 1차원 리스트 초기화
_n = 10
_list = [0]*_n
print(_list) # [0,0,0,0,0,0,0,0,0,0]
_list = [1,2,3,4,5,6,7]
print(_list[1:4]) # [2,3,4]

# 리스트 컴프리헨션 : 리스트 초기화 하는 방법 중 하나
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
_array = [i for i in range(20) if i % 2 == 1]
print(_array) #[1,3,5,7,..19]

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
_array = [i * i for i in range(1,10)]
print(_array) # [1,4,9,16,...64,81]

# 리스트 컴프리헨션을 이용한 2차원 리스트 초기화 
# N * M 크기의 2차원 리스트 초기화
# 주의점 : p423 , 2차원 리스트 초기화 시 리스트 컴프리헨션 사용
N = 3
M = 4
_array = [[0] * m for _ in range(N)]
print(_array) # [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
```



#### 리스트 관련 메소드

```python
_list = [1,4,3]

_list.append(2)
print(_list) # [1,4,3,2]

_list.sort()
print(_list) # [1,2,3,4]

_list.sort(reverse = True)
print(_list) # [4,3,2,1]

_list.reverse() # 원소 뒤집기
print(_list) # [1,2,3,4]

# 특정 인덱스에 데이터 추가
_list.insert(2,3) # 인덱스2에 '3' 추가
print(_list) # [1,2,3,3,4]

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 : ", _list.count(3)) # 값이 3인 데이터 개수 : 2

# 특정 값 데이터 삭제
_list.remove(1)
print(_list) # [2,3,3,4]

# 특정 값들을 모두 제거 방법
_list = [1,2,3,4,5,5,5]
remove_set = [3,5]
_result = [i for i in _list if i not in remove_set]
print(_result) # [1,2,4]
```



#### 튜플

```python
# 튜플은 한 번 선언된 값을 변경할 수 없다.
# 리스트는 대괄호를 이용하고 튜플은 소괄호를 이용
# 에러 예제

_tuple = (1,2,3)
print(_tuple) # (1,2,3)

a[2] = 7 # 에러 발생 , 튜플은 대입 연산자(=) 사용 불가
```



#### 사전 자료형

```python
data = dict()
data['사과'] = 'apply'
data['바나나'] = 'banana'
key_list = data.keys()
value_list = data.values()
```



#### 집합 자료형

```python
# 중복을 허용하지 않는다.
# 순서가 없다. 

# 초기화 방법 1
_data = set([1,1,2,3,4,4,5])
print(_data) # {1,2,3,4,5}

# 초기화 방법 2
_data = {1,1,2,3,4,4,5}
print(_data) # {1,2,3,4,5}

# 집합 자료형의 연산
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b) # 합집합
print(a&b) # 교집합
print(a-b) # 차집합

_data = set([1,2,3])
_data.add(4)
print(_data) # {1,2,3,4}

_data.update([5,6])
print(_data) # {1,2,3,4,5,6}

_data.remove(3)
print(_data) # {1,2,4,5,6}

# add(), remove() 모두 시간 복잡도 O(1)
```



#### 람다식

```python
# 람다식 표현 예제
print((lambda a,b : a + b)(3,7)) #10
```



#### 입출력

```python
# 입력을 위한 전형적인 코드
N = int(input())
# 각 데이터를 공백으로 구분하여 입력
_data = list(map(int,input().split()))

_data.sort(reverse = True)
print(_data)

# 또 다른 예제
n,m,k = map(int,input().split())
print(n,m,k)

# input()은 오래 걸려서 입력 개수가 많을 때는 sys 라이브러리 사용
# rstrip() 함수 꼭 호출 : 공백 문자 제거 ,readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력
import sys
_data = sys.stdin.readline().rstrip()
print(_data)
```


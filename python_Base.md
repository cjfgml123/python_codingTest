### 1. Python 주요 라이브러리

#### 1-1) 내장함수

```python
result = sum([1,2,3])
print(result) # 6

result = min(7,5,3)
print(result)  # 3

result = max(6,3,2)
print(result) # 6

result = eval("(3 + 5) * 7") # 수학 수식이 문자열 형식으로 들어오면 해당 수식 계산
print(result) # 56

result = sorted([6,1,3])
print(result) # [1,3,6]

result = sorted([6,1,3],reverse = True)
print(result) # [6,3,1]

# 람다식을 이용한 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬
result = sorted([('a',1),('b',6),('c',5)], key = lambda x : x[1], reverse = True)
print(result) #[('b',6),('c',5),('a',1)]
```



#### 1-2) itertools

- 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리

```python
from itertools import permutations # 객체에서 r개의 데이터를 뽑아 일렬로 나열, 모든 순열 계산

data = ['A','B','C']
result = list(permutations(data,3)) # data에서 3개를 뽑아 순열 구하기
print(result) 
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

from itertools import combinations 
result = list(combinations(data,2)) #순서를 고려하지 않는 2개를 뽑는 모든 조합 구하기
print(result)
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

from itertools import product
result = list(product(data,repeat = 2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기(중복허용)
print(result)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
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

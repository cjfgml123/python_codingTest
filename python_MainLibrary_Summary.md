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



#### 1-3) heapq

- 파이썬에서 힙 기능을 위해 heapq라이브러리 제공
- 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
- 파이썬의 힙은 최소 힙으로 구성되어 있어 단순히 원소를 넣는 것으로 오름차순 정렬이 완료된다. 최상단 원소는 항상 '가장 작은 원소'

```python
import heapq

def heapsort(iterable):
    h = [] # 값을 삽입할 리스트
    result = []
    
    for value in iterable:
        heapq.heappush(h,value) # 담기 heappush(heap,item)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,0])
print(result)
#[0,1,3,5,7]

# 최대 힙을 제공하지 않아 원소의 부호를 임시로 변경하여 작성(내림차순힙)
def heapReversSort(iterable):
    h = [] # 값을 삽입할 리스트
    result = []
    
    for value in iterable:
        heapq.heappush(h,-value) # 담기 heappush(heap,item)
    
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,0])
print(result)
#[7,5,3,1,0]
```



#### 1-4) bisect

- 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리 제공
- '정렬된 배열'에서 특정한 원소를 찾아야 할 때 효과적으로 사용된다.
  - bisect_left(a,x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메소드
  - bisect_right(a,x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메소드

```python
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

# 인덱스값 반환
# 리스트에서 4가 있는데 삽입할 가장 왼쪽 인덱스, 오른쪽 인덱스 반환
print(bisect_left(a,x)) # 2
print(bisect_right(a,x)) # 4

# 활용 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때, 사용
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a , right_value)
    left_index = bisect_left(a , left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
# 값이left_value, right_value에 속하는 데이터의 개수를 반환
print(count_by_range(a,4,4)) # 2  # 값이 4인 데이터 개수 출력
print(count_by_range(a,-1,3)) # 6 # 값이 [-1,3] 범위에 있는 데이터 개수 출력
```



#### 1-5) collections

- 보통 deque를 사용해 스택, 큐를 구현한다. (인덱싱, 슬라이싱 기능 사용 x)
- 연속적으로 나열된 데이터의 시작 부분이나 끝 부분에 데이터를 삽입하거나 삭제할 때는 효과적
- Counter는 등장 횟수를 세는 기능 제공

```python
# 첫 번째 원소를 제거할 때 popleft() 사용
# 마지막 원소를 제거할 때 pop() 사용

# 변수 x를 첫 번째 인덱스에 원소 삽입할 때 appendleft(x) 사용
# 마지막 인덱스에 삽입할 때 append(x) 사용

from collections import deque
data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data) # deque([1,2,3,4,5])
print(list(data)) # [1,2,3,4,5]

from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue']) # 3 
print(counter['green']) # 1
print(dict(counter)) #{'red':2,'blue':3,'green':1}
```



#### 1-6) math

- 팩토리얼, 제곱근, 최대공약수(GCD) 등을 계산해주는 기능을 포함

```python
import math

print(math.factorial(5)) # 5 팩토리얼을 출력
# 120

print(math.sqrt(7)) # 7 제곱근을 출력

print(math.gcd(21,14)) # 21과 14의 최대 공약수를 출력
```

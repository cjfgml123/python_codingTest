### 1. 정렬 알고리즘 기본 기론

- 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
- 이진 탐색의 전처리 과정에 사용



#### 1-1) 선택 정렬

- 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정

- 시간 복잡도 O(N**2)

  ```python
  array = [4,6,1,2,0]
  
  for i in range(len(array)):
      min_index = i
      for j in range(i + 1, len(array)):
          if array[min_index] > array[j]:
              min_index = j
      array[i], array[min_index] = array[min_index], array[i]
  print(array)
  ```

  

#### 1-2) 삽입 정렬

- 선택 정렬에 비해 실행 시간 측면에서 효율적

- 필요할 때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 효율적

- 특정한 데이터를 적절한 위치에 '삽입' 한다는 의미

- 두 번째 데이터 부터 시작, 첫 번째 데이터는 그 자체로 정렬되어 있다고 판단

- 시간 복잡도 O(N**2)

  ```python
  array = [4,6,1,2,0]
  
  for i in range(1,len(array)):
      for j in range(i,0,-1): # 인덱스 i부터 1(end+1)까지 감소하며 반복
          if array[j] < array[j - 1]:
              array[j],array[j - 1] = array[j - 1],array[j]
          else:
              break
  print(array)
  ```

  



#### 1-3 ) 퀵 정렬

- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 것.
- 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식
- 피벗(Pivot)사용 : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'을 피벗이라 표현
  - 피벗 설정 방법 : 대표적으로 호어 분할(Hoare Partition 방식)
  - 리스트에서 첫 번째 데이터를 피벗으로 정한다. 왼쪽에서 부터 피벗보다 큰 데이터를 찾고, 오른쪽에서 부터 피벗보다 작은 데이터를 찾은 후 위치를 서로 교환한다.
- 시간 복잡도 평균적으로 O(NlogN) 최악의 경우O(N**2)

```python
array = [4,6,1,2,0]

def quick_sort(array,start,end):
    if start >= end: # 원소가 1개인 경우 종료
        return
	pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right <= start and array[right] >= array[pivot]:
    		right -= 1
        
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[pivot], array[right] = array[right], array[pivot]
        else : # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left],array[right] = array[right],array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1) # right -1 인건 pivot과 right 인덱스 인 값을 교환
    quick_sort(array, right + 1, end)
            
quick_sort(array,0,len(array)-1)
print(array)

# 파이썬 장점을 살린 퀵 정렬 코드
def python_puick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return python_puick_sort(left_side) + [pivot] + python_puick_sort(right_side)

print(python_puick_sort(array))
    
```



#### 1-4) 계수 정렬(Count Sort)

- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
- 데이터의 개수가 N , 데이터 중 최댓값이 K일 때 계수 정렬은 최약의 경우에도 O(N+K)를 보장
- 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을때만 사용할 수 있음.
- 모든 범위를 담을 수 있는 크기의 리스트를 선언해야 함.

```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [5,6,4,3,2,1,2,0,4,8,9]

# 모든 범위 (0 ~ 9)를 갖는 인덱스의 리스트 선언
count = [0] * (max(array)+1) 

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력ㅂ
```



##### 1-5) 파이썬의 정렬 라이브러리

- 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어졌음.
- 일반적으로 병합 정렬은 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도 O(NlogN)을 보장

```python
array = [1,3,5,2]

# 방법 1
result = sorted(array)
print(result)

# 방법 2
array.sort()
print(array)

# 정렬 라이브러리에서 key를 활용한 소스
array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(array,key = setting)
print(result) # [('바나나',2),('당근',3),('사과',5)]
```


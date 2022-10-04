### 1. 이진탐색 알고리즘 기본 기론



#### 1-1) 순차 탐색

- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

- 최악의 경우 시간 복잡도 O(N)

  ```python
  def sequential_search(n,target,array):
      for i in range(n):
          if array[i] == target:
              return i+1 # 현재의 위치 반환(인덱스0으로 시작하므로 + 1)
  print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
  input_data = input().split()
  n = int(input_data[0])
  target = input_data[1]
  
  print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
  array = input().split()
  
  print(sequential_search(n,target,array))
  ```

  

#### 1-2) 이진 탐색 : 반으로 쪼개면서 탐색하기

- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘

- 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징

- 위치를 나타내는 변수 3개를 사용함. (범위의 시작점, 끝점, 중간점) , 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것.

- 시간 복잡도 : O(logN)

  ```python
  # 재귀 함수로 구현
  def binary_serach(array, target, start, end):
      if start > end:
          return None
      mid = (start + end) // 2
      if array[mid] == target:
          return mid
      elif array[mid] > target: 
          return binary_search(array,target,start,mid - 1)
      else:
          return binary_search(array,target,mid + 1, end)
  
  n, target = list(map(int,input().split()))
  array = list(map(int,input().split()))
  
  result = binary_search(array, target, 0, n - 1)
  if result = None:
      print("원소 존재 X")
  else:
      print(result + 1)
      
  # 반복문으로 구현한 이진 탐색 코드
  def binary_search(array, target, start, end):
      while start <= end:
          mid = (start + end) // 2
          if array[mid] == target:
              return mid
          elif array[mid] > target:
              end = mid - 1
          else:
              start = mid + 1
       return None
  
  ```

  


##### 1-3) 입력 데이터가 많을때는 input()은 느리므로

```python
import sys 
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()
print(input_data)
# rstrip() 호출 안하면 엔터가 줄바꿈 기호로 입력
```




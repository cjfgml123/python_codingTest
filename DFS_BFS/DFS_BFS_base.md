### 1. DFS/BFS를 위한 기본 이론

- 그래프를 탐색하기 위한 대표적인 두 가지 알고리즘

#### 

#### 1-1) 오버플로(Overflow) : 데이터의 크기를 가득 찬 상태에서 삽입 연산을 수행할때 발생

#### 1-2) 언더플로(Underflow): 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행할때 발생



#### 1-3 ) 스택 (Stack)

```python
# 파이썬에선 리스트에서 append()와 pop()으로 스택 구현
# First in Last Out 선입 후출
stack = []

stack.append(5) # 5 
stack.append(4) # 5 4 
stack.append(3) # 5 4 3 
stack.pop() # 5 4 

print(stack) # 5 4 , 최하단 원소부터 출력
print(stack[::-1]) # 4 5 ,최상단 원소부터 출력  [start:end:step]

```



#### 1-4) 큐 (Queue)

```python
# First in First Out 선입 선출

from collections import deque

queue = deque()

queue.append(1) # 1 
queue.append(2) # 2 , 1
queue.append(3) # 3, 2 ,1
queue.popleft() # 2,1

print(queue) # 먼저 들어온 순서대로 출력
queue.revese()
print(queue) # 나중에 들어온 원소부터 출력
# list(queue) 리스트 자료형으로 반환
```



#### 1-5) 재귀 함수(Recursive Function)

```python
# 2가지 방식으로 구현한 팩토리얼 예제

def factorial_iterative(n):
    result = 1
    
    for i in range(1,n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1: # 0! = 1 , 1! = 1
        return 1
    # n! = n * (n-1)!
    return n * factorial_recursive(n - 1)

```

#### 1-6) DFS (Depth-First Search) 깊이 우선 탐색

- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

- 노드(Node)와 간선(Edge)으로 표현

- 스택 자료구조를 이용

  - 동작과정 : 

    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리한다.

       2.스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.

    3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
       
       - 인접한 노드 중에서 방문하지 않은 노드가 여러 개 있으면 관행적으로 번호가 낮은 순서부터 처리 

##### 1-6-1) 그래프를 표현하는 2가지 방식

- 인접행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
- 인접 리스트(Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방식

```python
# 인접 행렬 방식 예제
INF = 999999999

graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
print(graph)

# 인접 리스트 방식 예제
graph = [[] for _ in range(3)] # 행 3개인 2차원 리스트
# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))
graph[2].append((0,5))
print(graph) # [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
```



##### 1-6-2) DFS 예제(재귀함수 이용)

```python
def dfs(graph, v, visited):
    visited[v] = True # 현재 노드를 방문 처리
    print(v, end= ' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]        

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

dfs(graph, 1, visited)
```



#### 1-7) BFS (Breadth First Search) 너비 우선 탐색

- 시작노드에서 가까운 노드부터 탐색하는 알고리즘
- 선입선출 방식인 큐 자료구조를 이용
  - 동작방식
    - 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
      2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
      3. 2.번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
      4. 숫자가 작은 노드부터 먼저 큐에 삽입 한다고 가정
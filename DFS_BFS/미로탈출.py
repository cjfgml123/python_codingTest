# 탈출하기 위한 최소 칸의 개수 구하기
from collections import deque
N , M = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input())))

# 상, 하 , 좌, 우로 갈 경우 [x][y]의 좌표 이동을 생각
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[N-1][M-1]
    
print(BFS(0,0))
    
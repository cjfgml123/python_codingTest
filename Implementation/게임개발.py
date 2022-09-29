# P118
N , M = map(int,input().split()) # N : 세로크기, M : 가로크기
x, y , dir = map(int,input().split())

_start = [[0] * M for i in range(N)]
_start[x][y] = 1 # 방문한 곳은 1로 처리

mapInfo = []
for i in range(N):
    mapInfo.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

_count = 1
turn_time = 0

def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

while(True):
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if _start[nx][ny] == 0 and mapInfo[nx][ny] == 0 :
        _count += 1 
        _start[nx][ny] = 1
        x,y = nx, ny
        turn_time = 0
        continue
    else :
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if mapInfo[nx][ny] == 0 :
            x,y = nx,ny
        else:
            break
        turn_time = 0

print(_count)
        
    
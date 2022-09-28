# (1,1) 을 시작으로 LRUD로 왼,오른,위,아래 방향으로 도착 좌표 찾기 , N * N 안에서만 
def self_solution():
    N = map(int,input())
    _valStrList = list(map(str,input().split()))
    _start = [1,1]
    
    for _valStr in _valStrList:
        if _valStr == 'L' and _start[1] > 1:
            _start[1] -= 1
        elif _valStr == 'R' and _start[1] < 5:
            _start[1] += 1
        elif _valStr == 'U' and _start[0] > 1:
            _start[0] -= 1
        elif _valStr == 'D' and _start[0] < 5:
            _start[0] += 1
        
    print(str(_start[0]) + " " + str(_start[1]))
    
def solution():
    n = int(input())
    x, y = 1, 1
    plans = input().split()
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    move_types = ['L','R','U','D']
    
    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        
        x, y = nx, ny
    print(x,y)

solution()
# 8*8 크기의 맵에서 시작좌표에서 move_type으로 갈 수 있는 경우의 수 구하기
def self_solution():
    _start = input()

    nx = ['a','b','c','d','e','f','g','h']
    ny = int(_start[1])
    move_type = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    count = 0

    for move in move_type:
        if (ny + move[1]) > 0 and (ny + move[1]) < 9 :
            for i in range(len(nx)):
                if _start[0] == nx[i]:
                    if (i + move[0]) >= 0 and (i + move[0] <= 7):
                        count += 1      

    print(count)       
    
def solution():
    input_data = input()
    row = int(input_data[1])
    # ord(문자) : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환 ex) ord('a') = 97
    column = int(ord(input_data[0])) - int(ord('a')) + 1
    steps = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]
        
        if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
            result += 1
    print(result)

solution()
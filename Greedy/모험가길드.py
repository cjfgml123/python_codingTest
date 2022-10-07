# N = int(input())
# _list = list(map(int,input().split()))

N = 5
_list = [2,3,1,2,2]
_list.sort()

result = 0 # 그룹
count = 0 # 현재 그룹에 포함된 모험가 수
# 2,3,3,3,3
# 1,2,2,2,3
for i in range(len(_list)):
    count += 1
    if _list[i] == count:
        result += 1
        count = 0

print(result)
        
        


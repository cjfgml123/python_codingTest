N = int(input())

_list = list(map(int,input().split()))
_list.sort()

target = 1
for i in range(len(_list)):
    if target < _list[i]:
        break
    target += _list[i]

print(target)
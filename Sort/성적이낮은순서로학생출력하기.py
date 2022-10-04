N = int(input())

_list = []
for _ in range(N):
    _val = input().split()   
    _list.append((_val[0],int(_val[1])))

def setting(data):
    return data[1]

_list.sort(key=setting)
# _list = sorted(_list, key = lambda student : student[1])

for _val in _list:
    print(_val[0],end = ' ')
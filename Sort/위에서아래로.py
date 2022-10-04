N = int(input())

_list = []
for _ in range(N):
    _list.append(int(input()))

_list.sort(reverse=True)

for i in _list:
    print(i, end=' ')

n , m = map(int,input().split())
_resultList = []
for i in range(n):
    _valList = list(map(int,input().split()))
    _resultList.append(min(_valList))
print(max(_resultList))


    
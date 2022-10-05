N = int(input())

_list = list(map(int,input().split()))
    
M = int(input())
_valList = list(map(int,input().split()))

_list.sort()

def Search(array, start, end, target):
    while start <= end:    
        mid = (start + end) // 2

        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return 'no'
        
_result = []
for target in _valList:
    _result.append(Search(_list,0,len(_list)-1,target))

for i in _result:
    print(i,end=' ')
    
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 문제집 풀이

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start <= end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in _valList:
    result = binary_search(_list, i, 0,N -1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no',end = ' ')
    

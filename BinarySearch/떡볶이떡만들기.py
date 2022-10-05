#N , M = map(int,input().spilt())
#_list = list(map(int,input().spilt()))

N , M = 4, 6
_list = [19,15,10,17]

def Search(_list, start, end):   
    result = 0
    while start <= end:
        length = 0 # 남은 떡 길이
        mid = (start + end) // 2 # 절단기 높이
        
        for i in _list:
            if i > mid:
                length += (i - mid)
            
        if M <= length:
            start = mid + 1
            result = mid
        
        elif M > length:
            end = mid - 1    
        else : # 같을때
            return mid 
    return result

            
print(Search(_list,0,max(_list)))
        
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 문제집 풀이

n, m = list(map(int,input().split(' ')))
array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid : # 자를때 떡 양 계산 작으면 0 이므로 조건 넣어주기 
            total += x - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기서 result 기록 
        start = mid + 1
print(result)
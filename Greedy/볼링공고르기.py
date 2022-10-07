N , M = map(int,input().split())
_list = list(map(int,input().split()))

_count = 0
for i in range(len(_list)-1):
    for j in range(i+1,len(_list)):
        if _list[i] != _list[j]:
            _count += 1

print(_count)        

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
array = [0] * 11

# 각 무게에 해당하는 볼링공의 개수 카운트
for i in _list:
    array[i] += 1

result = 0
# 1 부터 m까지의 각 무게에 대하여 처리
for i in range(1,M + 1):
    N -= array[i]  # 무게가 i인 볼링공의 개수 제외
    result += array[i] * N # B가 선택하는 경우의 수와 곱하기
print(result)
data = input()


_num = []
_str1 = []
for _str in data:
    try:
        _num.append(int(_str))
        
    except ValueError:
        _str1.append(_str)

_str1.sort()
if len(_num) != 0:  
    _str1.append(str(sum(_num)))

_result = ''
for _val in _str1:
    _result += _val
print(_result)

# ㅡㅡㅡㅡㅡㅡㅡㅡ풀이

result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()

if value != 0:
    result.append(str(value))
    
# '구분자'.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 구분자를 기준으로
# 'abc'의 문자열로 합쳐서 반환해주는 함수

print(''.join(result))
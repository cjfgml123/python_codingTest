def solution(left, right):
    answer = 0
    flag = True
    for i in range(left,right+1):
        for j in range(1,i+1):
            if j*j == i:
                flag = False
                break
        if flag:
            answer += i
        else:
            answer -= i
        flag = True
    return answer


# **0.5 는 제곱근 ex) 4**0.5 = 2 이것이 정수인 것은 약수 개수가 홀수개
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
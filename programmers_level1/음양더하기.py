
def solution(absolutes, signs):
    answer = 0

    for num,code in zip(absolutes,signs):
        if code:
            answer += num
        else:
            answer += num * -1
    return answer

def solution1(absolutes, signs):
    return sum(num if code else -num for num,code in zip(absolutes,signs))
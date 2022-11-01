def Mysolution(X, Y):
    answer = ''
    _listX = [0] * 10
    _listY = [0] * 10

    for i in range(0,10):
        _listX[i] = X.count(str(i))
        _listY[i] = Y.count(str(i))

    for i in range(9,-1,-1):
        if _listX[i] != 0 and _listY[i] != 0:
            if i == 0 and answer == '':
                return '0'

            if _listX[i] > _listY[i]:
                answer += str(i) * _listY[i]
            else:
                answer += str(i) * _listX[i]


    if answer == '':
        return '-1'

    return answer

def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
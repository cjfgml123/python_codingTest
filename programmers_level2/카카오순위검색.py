# 효율성 문제
def Mysolution1(info, query):
    answer = [0] * len(query)
    infoList = []
    for _info in info:
        _infoList = _info.split()
        infoList.append(_infoList)

    for i in range(len(query)):
        _queryList = query[i].split()
        _queryList = [i for i in _queryList if i != 'and']
        for _infoList in infoList:
            _bool = False
            for j in range(len(_queryList)):
                if j == len(_queryList) - 1:
                     if int(_infoList[j]) < int(_queryList[j]):
                        _bool = False
                else:
                    if _infoList[j] == _queryList[j] or _queryList[j] == '-':
                        _bool = True
                    else:
                        _bool = False
                        break
            if _bool:
                answer[i] += 1     
    
    return answer

from bisect import bisect_left
def Mysolution2(info, query):
    answer = []
    info_dict = {}
    
    # 조건 경우의 수 
    for _lan in ['cpp','java','python','-']:
        for _work in ['backend','frontend','-']:
            for _year in ['junior','senior','-']:
                for _food in ['chicken','pizza','-']:
                    info_dict[_lan+_work+_year+_food] = []
    # 지원자 경우의 수
    for _info in info:
        _infoList = _info.split()
        for _lan in [_infoList[0],'-']:
            for _work in [_infoList[1],'-']:
                for _year in [_infoList[2],'-']:
                    for _food in [_infoList[3],'-']:
                        info_dict[_lan+_work+_year+_food].append(int(_infoList[4]))
    
    for _keys in info_dict.keys():
        info_dict[_keys].sort()
    
    for _query in query:
        _queryList = _query.split()
        _queryList = [i for i in _queryList if i != 'and']
        _key = "".join(_queryList[:-1])
        _score = int(_queryList[-1])
        _index = bisect_left(info_dict[_key],_score)
        answer.append(len(info_dict[_key]) - _index)
    return answer
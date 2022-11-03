def solution(survey, choices):
    answer = ''
    _dict = {}
    
    _index = ['R','C','J','A']
    _score = [3,2,1,0,1,2,3]
    
    for sur in ['R','T','F','C','M','J','A','N']:
        _dict[sur] = 0
    
    for sur, cho in zip(survey,choices):
        if cho < 4:
            _dict[sur[0]] += _score[cho-1]
        elif cho > 4:
            _dict[sur[1]] += _score[cho-1]
        else:
            pass
    _beforeDict = {}
    _afterDict = {}
    
    for _key in _dict.keys():
        if _key in _index:
            _beforeDict[_key] = _dict[_key]
        else:
            _afterDict[_key] = _dict[_key]
    
    for key1,key2 in zip(_beforeDict.keys(), _afterDict.keys()):
        if _beforeDict[key1] > _afterDict[key2]:
            answer += key1
        elif _beforeDict[key1] < _afterDict[key2]:
            answer += key2
        else:
            answer += key1
          
    return answer
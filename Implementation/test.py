from collections import deque
def solution(progresses, speeds):
    answer = []
    
    progresses.reverse()
    speeds.reverse()
    count = 0
    
    while len(progresses) != 0 :
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        for i in range(len(progresses)-1,-1):
            if progresses[i] >= 100:
                count += 1
                answer.append(count)
            else:
                count = 0
                for _ in range(i):
                    if progresses[-1] >= 100:
                        progresses.pop()
                        speeds.pop()
                break
        
    return answer

print(solution([93,45],[1,30]))
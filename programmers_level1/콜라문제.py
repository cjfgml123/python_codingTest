import sys
sys.setrecursionlimit(10000) # case에 재귀함수 런타임 에러 있어서 씀.

def MySolution(a, b, n):
    answer = 0

    def recursive(n):
        nonlocal answer
        if n < a:
            return

        colla = (n // a) * b
        answer += colla
        colla += n % a
        recursive(colla)

    recursive(n)
    return answer

def Mysolution1(a, b, n):
    answer = 0

    while n >= a:
        cnt = (n // a) * b       
        answer += cnt
        cnt += n % a
        n = cnt
    return answer
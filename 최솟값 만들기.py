# https://school.programmers.co.kr/learn/courses/30/lessons/12941?language=python3

def solution(A,B):
    resultSum = 0
    
    A.sort()
    B.sort(reverse=True)
    
    for a, b in zip(A,B):
        resultSum += a * b

    return resultSum
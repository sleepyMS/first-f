# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):    
    root = [[-1 for i in range(m)] for j in range(n)]
    
    for i in range(m):
        if [i+1,1] in puddles:
            for j in range(i,m):
                root[0][j] = 0
            break
        else:
            root[0][i] = 1
    
    for i in range(n):
        if [1,i+1] in puddles:
            for j in range(i,n):
                root[j][0] = 0
            break
        else:
            root[i][0] = 1
            
    for i in range(1, n):
        for j in range(1, m):
            if [j+1,i+1] in puddles:
                root[i][j] = 0
            else:
                root[i][j] = root[i-1][j] + root[i][j-1]
    
    return root[n-1][m-1] % 1000000007
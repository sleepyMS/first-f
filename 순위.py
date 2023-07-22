def dfs(a, graph, game):
    stack = [a]
    visited = []
    
    while stack:
        current_num = stack.pop()
        visited.append(current_num)
        
        for i in graph[current_num]:
            if i not in visited:
                stack.append(i)
                
    visited.remove(a)
    visited = list(set(visited))
    game[a][1] += len(visited)
    for i in visited:
        game[i][0] += 1
        
    return

def solution(n, results):
    count = 0
    graph = {i: [] for i in range(1, n+1)}
    game = {i: [0,0] for i in range(1, n+1)}
    
    for result in results:
        graph[result[1]].append(result[0])
        
    for i in graph:
        dfs(i, graph, game)
        
    for i in graph:
        if sum(game[i]) == n - 1:
            count += 1
        
    return count
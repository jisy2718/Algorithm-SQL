def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    from collections import deque
    sr, sc, cost = 0,0,1
    q = deque([[sr, sc, cost]])
    visited = [[0]*m for _ in range(n)]
    visited[sr][sc] = 1
    while q:
        cr, cc ,c_cost = q.popleft()
        if cr == n-1 and cc == m-1:
            return c_cost
        
        for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
            nr = cr+dr
            nc = cc +dc
            if 0 <= nr <n and 0 <= nc <m and visited[nr][nc] == 0 and maps[nr][nc] == 1:
                visited[nr][nc] = 1
                q.append([nr,nc,c_cost+1])

    
    return -1
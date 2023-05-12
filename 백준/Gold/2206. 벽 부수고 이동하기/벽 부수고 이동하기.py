N, M = map(int,input().split())
arr = [ list(map(int,input())) for _ in range(N)]

sr, sc = 0, 0
er, ec = N-1, M-1
break_cnt = 0
move = 1

from collections import deque
visited = [ [[0]*M for _ in range(N)] for _ in range(2) ]

q = deque()
q.append([sr,sc, break_cnt, move])
visited[break_cnt][sr][sc] = 1
result = -1
while q:
    cr, cc, c_break_cnt, c_move = q.popleft()
    # 목표지점에 도달
    if cr == er and cc == ec:
        result = c_move
        break

    for delta in [[0,1],[0,-1],[1,0],[-1,0]]:
        dr, dc = delta
        nr = cr + dr
        nc = cc + dc
        # map을 벗어나지 않고, 이동 가능 하다면,
        if 0 <= nr < N and 0 <= nc < M and visited[c_break_cnt][nr][nc] == 0:
            # 1. 벽이 아닌 경우
            if arr[nr][nc] == 0 :
                q.append([nr, nc, c_break_cnt, c_move+1])
                visited[c_break_cnt][nr][nc] = 1

            # 2. 벽인 경우
            elif arr[nr][nc] == 1  and c_break_cnt == 0 :
                q.append([nr, nc, c_break_cnt+1, c_move+1])
                visited[c_break_cnt+1][nr][nc] = 1

print(result)
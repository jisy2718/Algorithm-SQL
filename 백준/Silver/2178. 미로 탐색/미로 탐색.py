# 배열 받기
N, M = map(int,input().split())

arr = []
for _ in range(N):
    row = list(map(int,input()))
    arr.append(row)

# visited 배열 생성
visited = [[0]*M for _ in range(N)]

# (0,0)에서 출발해서 (N-1, M-1)에 도착하는 bfs
## bfs초기화
sr, sc = 0,0
from collections import deque
q = deque([[sr,sc,1]]) # 행, 열, 이동한칸개수 (시작위치 포함)

## bfs 순회
while q:
    cr, cc, c_cnt = q.popleft()

    ### 목적지에 도착시, 처음 도착하는 것이 최단거리임.
    if cr == N-1 and cc == M-1:
        print(c_cnt)
        break

    ### 이동가능한 곳 탐색
    for move in [[0,-1], [0,1],[1,0],[-1,0]]:
        nr = cr + move[0]
        nc = cc + move[1]
        ### 이동가능하고 방문하지 않았으면 q에 넣기
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]== 1 and visited[nr][nc] == 0 :
            visited[nr][nc] = 1
            q.append([nr, nc, c_cnt+1])


N, M = map(int,input().split())

arr = []
for _ in range(N):
    row = list(map(int,input().split()))
    arr.append(row)

answer = 0
def dfs(r,c, total_sum, idx ):
    global answer
    if idx == 4 : # 4개 블록을 선택한 경우
        if answer < total_sum :
            answer = total_sum

        return

    else:

        for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                dfs(nr, nc, total_sum+arr[nr][nc], idx +1)
                visited[nr][nc] = 0


                if idx == 2: # 만약 2곳을 이미 방문했다면,ㅗ ,ㅓ , ㅜ, ㅏ 모양 방문하기 위해서
                    visited[nr][nc] = 1
                    dfs(r, c , total_sum+arr[nr][nc], idx +1)
                    visited[nr][nc] = 0

visited = [[0]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r,c,arr[r][c], 1)
        visited[r][c] = 0

print(answer)
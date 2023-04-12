T = int(input())
for tc in range(1,T+1):
    # 1. input 받기
    M, N, K = map(int,input().split()) # M 가로 / N 세로
    
    arr = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        c, r = map(int,input().split()) # 주의
        arr[r][c] = 1
    
    # 2. visited 생성
    visited = [[False]*M for _ in range(N)]
    
    
    # 3. 이동 규칙

    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    
    # 4. 전체 그룹 개수 초기화
    count = 0
    
    # for loop 2번으로 순회
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1 and visited[r][c] == False: # 방문
                count += 1
                stack = []
                stack.append([r,c])
                visited[r][c] = True
                while stack:
                    cr, cc = stack[-1]
                    
                    # 4방향 이동
                    for i in range(4):
                        nr = cr + dr[i]
                        nc = cc + dc[i]
                        # 조건 맞으면 stack에 추가
                        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == False and arr[nr][nc]==1:
                            stack.append([nr,nc])
                            visited[nr][nc] = True
                            break # 바로이동
                    else:
                        stack.pop()
                        
    print(count)
                    
              
    
N = int(input())
# 1. input / 1: 집, 0 : 집x
arr = [ list(map(int,input())) for _ in range(N)]


# 2. 이동 규칙 # 상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 3. visited
visited = [[False]*N for _ in range(N)]

# 4. 단지수, 단지별 크기
count = 0
result = []

# 5. 순회
# for 2번
    # 0 / 1 판단 + visited 판단
for r in range(N):
    for c in range(N):
        # 시작할 때, count / 하나의 단지를 찾은 것임
        if arr[r][c] == 1 and visited[r][c] == False:
            count += 1
            volume = 1
            # DFS 로 구현
            stack = []
            stack.append([r,c])
            visited[r][c] = True
            while stack:
                cr, cc = stack[-1]
                
                for i in range(4):
                    nr = cr + dr[i]
                    nc = cc + dc[i]
                    
                    # 조건 확인 후
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False and arr[nr][nc] == 1:
                        stack.append([nr,nc])
                        visited[nr][nc] = True
                        volume += 1
                        break
                        
                else:
                    stack.pop()
            result.append(volume)
            # 하나의 단지 탐색 끝
            
print(count)
result.sort()
for volume in result:
    print(volume)
            
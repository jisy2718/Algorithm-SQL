N = int(input()) # 컴퓨터 개수
M = int(input()) # 연결 개수

# 연결 관계 입력 받기
connection = [[0]*101 for _ in range(101)]
for _ in range(M):
    s, e = map(int,input().split())
    connection[s][e] = 1
    connection[e][s] = 1

# 방문 배열 생성
visited = [0]*101

# 감염된 컴퓨터 수 세기
cnt = -1

# dfs 정의하기
def dfs(cur):
    global cnt
    cnt += 1

    # 순회
    for next_com in range(1,101):
        if connection[cur][next_com] == 1 and visited[next_com] == 0: # 연결되어 있고, 방문하지 않았다면 바로 방문
            visited[next_com] = 1
            dfs(next_com) # dfs 이므로 갈 수 있는 곳 바로 방문

    return

# 순회 시작
visited[1] = 1
dfs(1)
print(cnt)
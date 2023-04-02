# 1. input
N, M, V = map(int, input().split())

adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int,input().split())
    adj[s][e] = 1
    adj[e][s] = 1





# 2. DFS
## [1] - 1 stack 버전 1
visited1 = [0]*(N+1)
stack1 = [V]
visited1[V] = 1
dfs_path1 = [str(V)]
while stack1:
    cur = stack1[-1]
    for v in range(1,N+1):
        if adj[cur][v] == 1 and visited1[v] == 0:
            visited1[v] = 1
            stack1.append(v)
            dfs_path1.append(str(v))
            break
    else:
        stack1.pop()

# print(' '.join(dfs_path1))


## [1] - 2 재귀 버전 1
# 함수호출이 stack에 append 하는 것이고, 함수 끝나는 것이 stack에서 pop임.
# cur  번 노드에서 경로 찾기
def dfs(cur):  # 이 함수 시작하면, v 번 노드로 이동한다는 의미
    visited2[cur] = 1  # v번 노드 방문 표시
    dfs_path2.append(str(cur))
    for v in range(1 , N+1):
        if adj[cur][v] == 1 and visited2[v]==0:  # 방문하지 않은 이동할 곳이 있으면 바로 이동
            dfs(v)

    return # 이동할 곳이 없다면 이전 위치로 되돌아가기

visited2 = [0]*(N+1)
dfs_path2 = []
dfs(V)  # V번 노드에서 길찾기 시작
print(' '.join(dfs_path2))



# 3. BFS
## [1] queue 버전
from collections import deque
q = deque([V])
bfs_path = [V]  # queue에 넣는 것이 이동하는 것!
visited3 = [0]*(N+1)
visited3[V] = 1
while q:
    cur = q.popleft()
    for v in range(1,N+1):
        if adj[cur][v] == 1 and visited3[v]==0:
            q.append(v)
            visited3[v] = 1
            bfs_path.append(v)

print(' '.join(map(str,bfs_path)))


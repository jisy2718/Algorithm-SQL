import sys
input = sys.stdin.readline
# 배열 받기
V, E = map(int,input().split())
start = int(input())

arrL = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int,input().split()) # 시작, 종료, 가중치
    arrL[s].append([e,w])


# 초기화
INF = 0xffffffff
cost = [INF]*(V+1)


# 다익스트라
## 1. 방문 후에 최소비용 update
## 2. 최소 비용인 곳 찾고 방문

visited = [0]*(V+1)
visited[start] = 1
cost[start] = 0

cur_node = start
while True:
    ## 1. 방문 후에 최소비용 update
    for neighbor, cur_to_next_cost in arrL[cur_node]:
        if cost[neighbor] > cost[cur_node] + cur_to_next_cost:
            cost[neighbor] = cost[cur_node] + cur_to_next_cost

    ## 2. 최소 비용인 곳 찾고 방문
    min_cost = INF
    min_node = -1
    for node in range(1,V+1):
        if visited[node] == 0 and cost[node] < min_cost:
            min_cost = cost[node]
            min_node = node

    ### 최소인 곳으로 이동
    if min_node != -1:
        cur_node = min_node
        visited[cur_node] = 1

    ### 만약 이동 할 곳이 없으면 그만하기
    else:
        break

for node in range(1,V+1):
    if cost[node] == INF:
        print('INF')
    else:
        print(cost[node])
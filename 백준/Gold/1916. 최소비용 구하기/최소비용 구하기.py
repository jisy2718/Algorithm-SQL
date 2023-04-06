# 그래프 생성
N = int(input()) # 도시 개수 == 노드 개수
M = int(input()) # 버스 개수 == 간선 개수

arrL = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int,input().split())
    arrL[s].append([e,w])

# 출발, 도착지
start, end = map(int,input().split())

# 다익스트라 초기화
INF = 0xfffffff
min_cost_lst = [INF]*(N+1)  # index에 해당하는 노드 까지 이동 비용 초기화
min_cost_lst[start] = 0

visited = [0]*(N+1)    # index에 해당하는 노드 방문 여부
visited[start] = 1

# 다익스트라 구현
""" 다음을 반복
1. cur_node(최단거리)를 경로에 포함시킨 후, 최소 비용으로 이동할 수 있는 곳들 update
2. 최소 비용으로 이동할 수 있는 곳으로 이동하고, visited 표시
"""

cur_node = start
while visited[end] == 0: # 도착지에 도착할 때까지 반복

    ## 1. cur_node(최단거리)를 경로에 포함시킨 후, 최소 비용으로 이동할 수 있는 곳들 update
    for neighbor_node, cost in arrL[cur_node]:  # 각 노드까지 최소 비용으로 update
        if min_cost_lst[neighbor_node] > min_cost_lst[cur_node] + cost:
            min_cost_lst[neighbor_node] = min_cost_lst[cur_node] + cost

    ## 2. 최소 비용으로 이동할 수 있는 곳으로 이동하고, visited 표시
    min_cost = INF
    min_node = -1

    ### 2.1. 최소비용 인덱스 찾기
    for node in range(1,N+1):
        cost = min_cost_lst[node]
        if visited[node] == 0 and min_cost > cost:
            min_cost = cost
            min_node = node

    ### 2.2. 최소인 곳 방문하기
    visited[min_node] = 1
    cur_node = min_node

# 결과 출력
print(min_cost_lst[end])

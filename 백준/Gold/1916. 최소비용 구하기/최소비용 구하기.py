# 입력
N = int(input()) # 도시 개수
M = int(input()) # 버스 개수

arr = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int,input().split()) # 시작, 종료, 비용
    arr[s].append([e,w])

start, end = map(int,input().split()) # 시작점, 목적지

# 다익스트라
def dijkstra(start, end):
    visited = [0]*(N+1)
    INF = 0xfffffffff
    cost_lst = [INF]*(N+1)  # 이동비용 초기화
    cost_lst[start] = 0
    visited[start] = 1

    cur_node = start
    while visited[end] == 0:
        # 1. 가장 저렴한 곳으로 이동 후, 가격 update
        for neighbor, cur_to_next_cost in arr[cur_node]:
            if cost_lst[neighbor] > cost_lst[cur_node] + cur_to_next_cost:
                cost_lst[neighbor] = cost_lst[cur_node] + cur_to_next_cost

        # 2. 가장 저렴한 곳 찾아서 이동하기
        ## 2.1. 찾기
        min_cost = INF
        min_node = 0
        for node in range(1,N+1):
            if visited[node] ==0:
                if cost_lst[node] < min_cost:
                    min_cost = cost_lst[node]
                    min_node = node
        ## 2.2. 이동하기
        visited[min_node] = 1
        cur_node = min_node

    print(cost_lst[end])
    return

dijkstra(start,end)

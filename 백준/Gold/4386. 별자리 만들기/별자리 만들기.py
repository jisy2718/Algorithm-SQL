n = int(input())
cost_arr = [[0]*n for _ in range(n)]
loc_dict = {}
for i in range(n):
    x, y = map(float,input().split())
    loc_dict[i] = (x,y)

# 비용 update
for i in range(n):
    for j in range(i+1, n):
        xi, yi = loc_dict[i]
        xj, yj = loc_dict[j]
        cost = ((xi-xj)**2 + (yi-yj)**2)**(0.5)
        cost_arr[i][j]= cost
        cost_arr[j][i] = cost

# prim 알고리즘 이용
## 초기화
mst = [0]*n
start = 0
mst[start] = 1

INF = 0xffffffff
total_cost = 0

## 연결
for _ in range(n-1):
    ## 1. 최소 비용 이웃 찾기
    min_node = -1
    min_cost = INF
    for in_mst in range(n):
        if mst[in_mst] == 1 :
            for neighbor in range(n):
                if mst[neighbor] == 0 and cost_arr[in_mst][neighbor] < min_cost :
                    min_cost = cost_arr[in_mst][neighbor]
                    min_node = neighbor
    
    ## 2. 최소 비용 이웃을 tree에 연결하기
    mst[min_node] = 1
    total_cost += min_cost

print(round(total_cost,2))


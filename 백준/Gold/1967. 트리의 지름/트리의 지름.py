# 트리의 지름을 찾는 방법은 아래와 같다.
"""
1. 임의의 노드 A에서 가장 먼 노드 B를 찾는다.
2. 그러면 B는 지름의 한 지점이 된다.
3. B에서 가장 먼 노드 C를 찾는다.
4. 그러면 B-C는 트리의 지름이 된다.

위의 1.과같은 방식이 가능한 이유는,
    1단계 )  (아래에서 -는 경로를 의미함)
    우선 A에서 가장 먼 노드가 a라고 할때, 트리의 지름 B-C와 A-a가 x에서 만난다면, a는 B또는 C여야 한다.
    그 이유는 B-x-C가 지름이므로 x에서 갈 수 있는 곳 중 가장 먼 곳은 B 또는 C이다. 그렇지 않다면 B-x-C가 지름이 될 수 없다.
    따라서 A에서 가장 먼 노드를 잇는 선과 지름 B-C가 만난다면 -> a는 B또는 C이다.

    2단계 ) A에서 가장 먼 노드가 a라고 할때, 그 사이에 트리의 지름 B-C와 만나지 않는다고 가정해보자. 그리고 모순 임을 보이자.
      2-1) B에서 a로가는 최대거리 중 A-y-a와  B-y-a 꼴로 y에서 A-a와 만난다고 하자(a는 leaf이므로 무조건 만남). 그럼 A-y-B < A-y-a => y-B < y-a 가 성립한다.
      여기서 y-B사이에는 B-C 사이의 노드 z가 존재한다.(B,C는 모두 leaf이기 때문에 무조건 존재)
      y-z-B < y-a 인데, 그러면 C-B = C - z - B < C - z - y -a 가 되어 C-B가 지름이라는 것에 모순이다.

      따라서 가정이 잘못 되었다.
"""

import sys
sys.setrecursionlimit(10 ** 9)
# 입력
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    ## 양방향 이동 가능한 그래프이므로 아래처럼 받는다.
    p, c, w = map(int,input().split())
    graph[p].append([c,w])
    graph[c].append([p,w])

# 최장거리 찾는 dfs 함수구현
def dfs(cur_node, sum_weight):
    for neighbor, cur_to_next_weight in graph[cur_node]:
        if visited[neighbor] == -1:
            visited[neighbor] = sum_weight+cur_to_next_weight
            dfs(neighbor, sum_weight+cur_to_next_weight)

# 시작하기
## 지름의 한쪽끝점 찾기
visited = [-1]*(N+1)
visited[1] = 0
dfs(1, 0)
start_node = 0
max_val = 0
for node in range(1,N+1):
    if visited[node] > max_val:
        max_val = visited[node]
        start_node = node

## 지름의 반대쪽 끝점 찾기
visited = [-1]*(N+1)
visited[start_node] = 0
dfs(start_node, 0)
end_node = 0
max_val = 0
for node in range(1,N+1):
    if visited[node] > max_val:
        max_val = visited[node]
        end_node = node

print(max_val)
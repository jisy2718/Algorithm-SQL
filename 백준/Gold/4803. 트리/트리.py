import sys

input = sys.stdin.readline


def find_set(x):
    if make_set[x] == x:
        return x
    else:
        return find_set(make_set[x])

def union(a,b):
    root_a = find_set(a)
    root_b = find_set(b)
    make_set[root_b] = root_a # b를 a에 합치기


tc = 0
while True:
    tc += 1
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    # 그래프 정보 가져오기
    graph = [[] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)


    # make_set
    make_set = [x for x in range(n+1)]

    # cycle 요소들 넣어두기
    cycle_nodes = []

    # 트리 만들기
    for v in range(1,n+1):
        for neighbor in graph[v]:
            # 이미 대표원소가 같다면, 사이클이 생기는 것
            if find_set(v) == find_set(neighbor):
                cycle_nodes.append(v)
            # 합쳐주기
            union(v,neighbor)  # v의 이웃들은 v의 대표원소를 대표원소로 가짐

    # print(cycle_nodes)

    # 연결 요소 개수 세기(tree 와 cycle 있는 연결요소로 구성됨)
    result = 0
    for node in range(1, n+1):
        if make_set[node] == node:
            result += 1

    # cycle 있는 연결 요소 개수 빼주기
    cycle_root_nodes = set()
    for cycle_node in cycle_nodes:
        root = find_set(cycle_node)
        cycle_root_nodes.add(root)
    result -= len(cycle_root_nodes)



    # 결과 프린트
    if result == 0:
        print(f'Case {tc}: No trees.')
    elif result == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {result} trees.')

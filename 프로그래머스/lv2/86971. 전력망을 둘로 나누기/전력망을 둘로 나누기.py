def solution(n, wires):
    answer = -1
    
    tree = [[0]*(n+1) for _ in range(n+1)]
    for connection in wires:
        s,e = connection
        tree[s][e] = 1
        tree[e][s] = 1
    
    def find_node_num(cur_node):
        nonlocal cnt
        cnt += 1
        
        for node in range(1, n+1):
            if visited[node] == 0 and tree[cur_node][node] == 1:
                visited[node] = 1
                find_node_num(node)
    
    min_diff = 0xfffffff
    for connection in wires:
        s,e = connection
        # 연결 끊기
        tree[s][e] = 0
        tree[e][s] = 0
        
        cnt_list = []
        visited = [0]*(n+1)
        for node in range(1,n+1):
            if visited[node] == 0:
                visited[node] = 1
                cnt = 1
                find_node_num(node)
                cnt_list.append(cnt)
        
        min_diff = min(min_diff, abs(cnt_list[0]-cnt_list[1]))
        
        # 다시 연결해주기
        tree[s][e] = 1
        tree[e][s] = 1
        
        
        
    return min_diff
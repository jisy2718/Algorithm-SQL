import sys
input = sys.stdin.readline

V, E = map(int,input().split())
edges = []
for _ in range(E):
    s, e, w = map(int,input().split())
    edges.append([w, s, e])

# make set
p = [x for x in range(V+1)]

# find set
def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])



def union(x,y):
    root_x = find_set(x)
    root_y = find_set(y)
    p[root_y] = root_x

MST = list(range(1,V+1))
w_sum = 0
# sorting
# cycle 안생기면 선택
# 다 선택하면 끝

edges.sort()
for i in range(E):
    w, s, e = edges[i]
    if find_set(s) != find_set(e):
        union(s,e)
        w_sum += w
print(w_sum)

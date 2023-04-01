def dfs(x,count):
    global min_count
    # 백트래킹
    if count > min_count:
        return
    
    # 베이스라인
    if x == 1:
        if min_count > count:
            min_count = count

    else:
        if x % 3 == 0:
            dfs(x//3, count+1)

        if x % 2 == 0:
            dfs(x//2, count+1)

        dfs(x-1, count+1)
    return

N = int(input())
min_count = 0xffffff
dfs(N,0)
print(min_count)
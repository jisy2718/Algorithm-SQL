x = int(input())


cnt = [0]*(x+1) # cnt에는 index 의 숫자가 1이 되기 위해 필요한 이동횟수를 채워 넣을 것. 현재는 index가 1인 경우만 참.

for loc in range(2, x+1):
    cnt[loc] = cnt[loc-1] + 1  # 1칸 이동하는 것이 무조건 가능
    if loc%2==0: # 만약 현재 위치가 2로 나눠떨어진다면, 거리를 더 줄일 수 있음
        cnt[loc] = min(cnt[loc//2] + 1, cnt[loc])

    if loc%3 == 0: # 만약 현재 위치가 3으로 나눠떨어진다면, 거리를 더 줄일 수 있음
        cnt[loc] = min(cnt[loc//3] + 1, cnt[loc])

print(cnt[x]) # x를 1로 만드는데 드는 최소 횟수
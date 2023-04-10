# input 받기
N, K = map(int,input().split()) # item 개수 N, 최대 무게 K


items = [] # (weight,value)
for _ in range(N):
    w, v = map(int,input().split())
    items.append((w,v))


# dp 초기화
backpack = [0]*(K+1) # idx : 무게 w, value : 가치 v

# dp 진행
for w, v in items:   # 각 loop 때까지 나온 item만 존재한다고 가정하고 가방을 채우는 것임.
    # 전체 무게 K에서부터 앞으로 오면서 채우기 (작은 무게부터 K로 가면 아래의 max에서 갱신된 값을 또 이용하게 됨)
    for weight in range(K, w-1, -1): # w만큼의 무게를 넣을 것이므로 w까지 진행
        backpack[weight] = max(backpack[weight], backpack[weight-w] + v) # 백팩에 안넣기 / 넣기

# 결과 출력
print(backpack[K])
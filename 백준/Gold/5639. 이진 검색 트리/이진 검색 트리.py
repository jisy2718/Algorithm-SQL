import sys
sys.setrecursionlimit(10 ** 9)
# 1. input
pre_order_lst = []
while True:
    try:
        pre_order_lst.append(int(input()))
    except:
        break

# print(pre_order_lst)

# dfs 정의
def post(start_idx, end_idx):

    # 1. base
    ## start_idx < end_idx 인 경우에 더 이상 자식이 없는 것!
    if start_idx > end_idx:
        return

    # 2. 재귀
    cur_root_value = pre_order_lst[start_idx]
    right_root_idx = end_idx + 1
    for idx in range(start_idx+1, end_idx+1):
        if cur_root_value < pre_order_lst[idx]:
            right_root_idx = idx
            break
    # 왼편
    post(start_idx +1, right_root_idx-1)

    # 오른편
    post(right_root_idx, end_idx)

    # 왼편, 오른편 모두 탐색 후, 자신 print가 후위탐색
    print(cur_root_value)

# 실행
post(0,len(pre_order_lst)-1)
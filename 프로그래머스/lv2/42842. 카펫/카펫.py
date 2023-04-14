def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    # r <= c
    for r in range(2, total+1):
        if total % r == 0:
            c = total//r
            if r > c:
                break
            else:
                if (r-2)*(c-2) == yellow:
                    return [c,r]
    
    # return answer
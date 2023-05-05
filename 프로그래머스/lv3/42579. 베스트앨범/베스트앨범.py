def solution(genres, plays):
    answer = []
    
    # 1. 데이터 모으기
    play_cnt = {}
    genre_sort = {}
    for idx, genre_play in enumerate(zip(genres, plays)):
        genre, play = genre_play
        
        # 전체 장르 개수 세기
        if genre in play_cnt:
            play_cnt[genre] += play
        else:
            play_cnt[genre] = play
        
        # 각 장르별로 play 순위 정렬
        if genre in genre_sort:
            genre_sort[genre].append([-play, idx]) # sort 이용해서 -play, idx 둘 다 작은 순으로 정렬할 예정.
        
        else:
            genre_sort[genre] = [[-play, idx]]
            
    # 2. 정렬하기
    ## 2.1. 전체 장르 정렬
    play_sort = []
    for genre, cnt in play_cnt.items():
        play_sort.append([-cnt, genre])
    
    play_sort.sort()
    ## 2.2. 장르별로 정렬
    for value in genre_sort.values():
        value.sort()
    
    # 3. 출력하기
    ## 3.1. 장르 순서별로 출력
    for _, genre in play_sort:
        ## 3.2. 장르 내에서 출력
        genre_songs = genre_sort[genre]
        if len(genre_songs) >= 2:
            answer.extend([genre_songs[0][1], genre_songs[1][1]])
        else:
            answer.extend([genre_songs[0][1]])
    
    return answer
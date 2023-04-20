# Write your MySQL query statement below

select round(count(first_date)/count(distinct a.player_id),2) fraction from Activity a # 첫접속일 다음날에 접속자수 / 전체 수

# 각 유저별로 첫 접속일을 구하기
left join (select player_id, min(event_date) first_date from Activity group by player_id) tmp
on a.player_id = tmp.player_id
and datediff(event_date, first_date) = 1  # 현재 접속일이 첫접속일 +1 인 경우에만 join되도록!
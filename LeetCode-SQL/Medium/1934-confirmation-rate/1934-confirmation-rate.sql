# Write your MySQL query statement below
# 요청이 없는 user_id도 0으로 해줘야하기 때문에, Signups table에 Confirmations table을 left join하여, 모든 user_id를 고려할 수 있게 세팅
select s.user_id, round(sum(if(action='confirmed', 1, 0))/count(*),2) confirmation_rate from Signups s
left join Confirmations c
on s.user_id = c.user_id

group by s.user_id
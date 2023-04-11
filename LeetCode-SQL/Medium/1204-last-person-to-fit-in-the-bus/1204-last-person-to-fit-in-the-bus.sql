# Write your MySQL query statement below
select  q1.person_name person_name  from Queue q1

# join이 부등호로도 되는 군!
left join Queue q2
on q1.turn >= q2.turn

# 각 turn 이하의 모든 turn의 weight를 더하면 누적값을 구할 수 있음
group by q1.turn
having(sum(q2.weight) <= 1000)

# 조건에 맞는 1명을 찾기 위해 조절
order by q1.turn desc
limit 1
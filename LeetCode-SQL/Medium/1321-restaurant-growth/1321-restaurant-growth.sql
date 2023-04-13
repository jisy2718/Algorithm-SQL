# Write your MySQL query statement below

# 아이디어 : 각 visited_on마다 7일치의 visited_on과 amount를 left join 시켜서 group by로 집계해서 구하기
select c1.visited_on, sum(c2.amount) amount, round(avg(c2.amount),2) average_amount from 

(select visited_on, sum(amount) amount from Customer group by visited_on) c1
left join (select visited_on, sum(amount) amount from Customer group by visited_on) c2

# 7일이내인 것들만 join
on datediff(c1.visited_on,c2.visited_on) <=6
and datediff(c1.visited_on, c2.visited_on)>=0

group by c1.visited_on
having count(*) = 7 # 7일 모두 존재하는 경우만 select 하기 

# Write your MySQL query statement below
select s.product_id, s.year first_year, s.quantity, s.price from Sales s

# 최초 판매년을 table로 만들어서 join 시킴
left join (select product_id, min(year) first_year from Sales
group by product_id) f
on s.product_id = f.product_id

where s.year = f.first_year  # 첫 해인 경우 가져오기
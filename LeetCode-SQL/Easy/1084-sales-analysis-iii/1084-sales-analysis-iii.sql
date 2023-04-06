select p.product_id  , p.product_name  from Product p

# 오직 타겟 쿼터에만 팔린 상품인 경우1, 아닌 경우 0으로 표기
left join
(select product_id, if(min(sale_date  )>='2019-01-01' and max(sale_date) <= '2019-03-31', 1, 0) only_target_quarter from Sales
group by product_id) otq
on p.product_id = otq.product_id

where otq.only_target_quarter = 1




















































# select p.product_id, product_name from Product p
# left join Sales s
# on p.product_id = s.product_id 
# group by p.product_id
# having min(sale_date) >= '2019-01-01' and max(sale_date) <= '2019-03-31'






























































# Write your MySQL query statement below
# select p.product_id, p.product_name from product p
# left join sales s
# on p.product_id = s.product_id
# group by p.product_id
# having min(s.sale_date) > "2019-01-01" and max(s.sale_date) <"2019-03-31"
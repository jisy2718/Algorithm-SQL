# Write your MySQL query statement below
select product_name, sum(unit) unit from Products p
left join Orders o
on p.product_id = o.product_id
# and o.order_date like '2020-02%'
and extract(year_month from o.order_date) = 202002

group by p.product_name
having sum(unit) >=100
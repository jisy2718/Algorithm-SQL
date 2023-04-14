# Write your MySQL query statement below
# GROUP_CONCAT(distinct(field_name) ORDER BY filed_name) 이용!

select sell_date, count(distinct(product)) num_sold, group_concat(distinct(product) order by product asc) products
from Activities
group by sell_date
order by sell_date
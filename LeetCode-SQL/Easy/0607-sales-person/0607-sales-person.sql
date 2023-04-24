# Write your MySQL query statement below
# 'RED' 와 거래가 있는 sales_id 구한 후, 해당 목록에 없는 sales_id 구하기
select s.name from SalesPerson s
where s.sales_id not in 

(select o.sales_id from Orders o
left join Company c
using (com_id)
where c.name = 'RED')
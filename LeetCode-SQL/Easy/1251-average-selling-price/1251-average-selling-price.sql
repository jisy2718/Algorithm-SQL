# Write your MySQL query statement below

select p.product_id, round(sum(price*units)/sum(units),2) average_price from Prices p

# product_id 와 구매날짜 기준으로 join
left join (select * from UnitsSold group by product_id, purchase_date, units) u
on p.product_id = u.product_id
and p.start_date <= u.purchase_date 
and u.purchase_date <= p.end_date

group by product_id
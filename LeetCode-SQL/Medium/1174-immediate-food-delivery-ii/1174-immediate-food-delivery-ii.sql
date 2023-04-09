# 첫 주문인데 즉시 배달 주문인 비율 찾기
select round(sum(if(first_order = customer_pref_delivery_date,1, 0))/count(*)*100,2) immediate_percentage from Delivery d

# 첫 주문 날짜 join
left join (select customer_id, min(order_date) first_order from Delivery group by customer_id) tmp
on d.customer_id = tmp.customer_id 

# 첫 주문인 경우만 선택
where first_order = order_date
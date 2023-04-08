select u.user_id buyer_id , u.join_date , count(o.buyer_id ) orders_in_2019 from Users u
left join Orders o
on u.user_id = o.buyer_id
and order_date like '2019%'
group by u.user_id


















# select u.user_id buyer_id , u.join_date join_date , count(o.buyer_id) orders_in_2019 from Users u
# left join Orders o
# on u.user_id = o.buyer_id
# and o.order_date like '2019%'
# group by u.user_id

























































# # Write your MySQL query statement below
# select u.user_id buyer_id, u.join_date, count(order_date) orders_in_2019 from users u
# left join orders o
# on u.user_id = o.buyer_id
# and o.order_date like"2019%"
# group by u.user_id



# select * from users u
# left join orders o
# on u.user_id = o.buyer_id
# and o.order_date like"2019%"
# group by u.user_id




# Write your MySQL query statement below
# select * from users u
# left join orders o
# on u.user_id = o.buyer_id
# where o.order_date like"2019%"
# group by u.user_id


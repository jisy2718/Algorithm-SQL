# Write your MySQL query statement below
select p.product_id, if(lastest_date is null , 10, new_price) price from Products p

# 2019년 8월 16일 기준 최신 가격 업데이트 날짜 join
left join (select product_id, max(change_date) lastest_date from Products where change_date <= '2019-08=16' group by product_id) tmp
on p.product_id = tmp.product_id


where lastest_date is null  # 가격 변동 없던 제품들
or change_date = lastest_date  # 8월 16일 포함 이전에 가격 변동 있던 제품들

group by p.product_id, lastest_date
-- 코드를 입력하세요
SELECT p.product_id PRODUCT_ID, p.product_name PRODUCT_NAME, sum(price*amount) TOTAL_SALES from FOOD_PRODUCT p
inner join FOOD_ORDER o
on p.product_id = o.product_id
and o.produce_date like '2022-05%'

group by p.product_id, p.product_name

order by TOTAL_SALES desc, PRODUCT_ID ASC
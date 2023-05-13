-- 코드를 입력하세요
# SELECT * FROM

# (SELECT J.FLAVOR, J.TOTAL_ORDER + COALESCE(H.TOTAL_ORDER , 0) SUM_ORDER FROM JULY J
# LEFT JOIN FIRST_HALF H
# USING(SHIPMENT_ID)

# ORDER BY SUM_ORDER DESC) TMP

# LIMIT 3




SELECT FLAVOR FROM
(SELECT FLAVOR , J.TOTAL_ORDER + COALESCE(H.TOTAL_ORDER , 0) SUM_ORDER 
FROM ( SELECT FLAVOR, SUM(TOTAL_ORDER) TOTAL_ORDER FROM JULY GROUP BY FLAVOR) J
LEFT JOIN FIRST_HALF H
USING(FLAVOR)

ORDER BY SUM_ORDER DESC
) TMP
LIMIT 3
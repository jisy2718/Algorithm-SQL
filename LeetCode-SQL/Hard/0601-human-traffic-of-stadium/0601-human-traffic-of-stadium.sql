SELECT id, visit_date, people
FROM (
  SELECT *, COUNT(*) OVER (PARTITION BY island) AS cnt  # island로 group by해서 row개수 세기(island 크기 세기)
  FROM (
    # 핵심부분!! 100이상의 연속된 row들에 같은 숫자를 배정함 by island
    SELECT *, id - ROW_NUMBER() OVER (ORDER BY id) AS island
    FROM Stadium
    WHERE people >= 100
  ) AS subquery
) AS subquery2
WHERE cnt >= 3  # island의 크기가 3개 이상인 것들만 가져오기
ORDER BY visit_date;
-- 코드를 입력하세요
SELECT 
USER_ID, 
NICKNAME, 
CONCAT( CITY ,' ', STREET_ADDRESS1 ,' ', STREET_ADDRESS2) 전체주소,
CONCAT (SUBSTR(TLNO,1,3), '-', SUBSTR(TLNO,4,4), '-', SUBSTR(TLNO,8,4)) 전화번호  # STBSTR(COLNAME, START 위치, 개수)

FROM USED_GOODS_USER

# 3개 이상 게시글 있는 유저 찾기
WHERE USER_ID IN (
    SELECT WRITER_ID FROM USED_GOODS_BOARD
GROUP BY WRITER_ID
HAVING COUNT(*)>=3)

ORDER BY USER_ID DESC
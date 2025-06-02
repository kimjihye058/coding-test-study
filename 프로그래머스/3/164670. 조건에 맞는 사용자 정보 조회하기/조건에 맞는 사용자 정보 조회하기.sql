select USER_ID,	NICKNAME
, city ||' '|| STREET_ADDRESS1 ||' ' || STREET_ADDRESS2 as "전체주소"
, substr(TLNO, 1, 3) || '-' || substr(TLNO, 4, 4) || '-' || substr(TLNO, 8, 4) as "전화번호"
from USED_GOODS_USER
where USER_ID in (
select WRITER_ID 
from USED_GOODS_BOARD
group by WRITER_ID
having count(*) >= 3
)
order by 1 desc
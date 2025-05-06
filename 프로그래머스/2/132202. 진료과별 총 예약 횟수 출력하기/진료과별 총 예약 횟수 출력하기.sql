SELECT MCDP_CD as "진료과코드",
       count(*) as "5월예약건수"
FROM APPOINTMENT
WHERE TO_CHAR(APNT_YMD, 'yymm') = '2205'
GROUP BY MCDP_CD
ORDER BY count(*),mcdp_cd;
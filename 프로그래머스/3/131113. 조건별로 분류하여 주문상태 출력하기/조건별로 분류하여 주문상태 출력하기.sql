SELECT    ORDER_ID
        , PRODUCT_ID
        , TO_CHAR(OUT_DATE, 'YYYY-MM-DD') "출고일자"
        , CASE WHEN OUT_DATE <= TO_DATE('20220501', 'YYYYMMDD') THEN '출고완료'
               WHEN OUT_DATE > TO_DATE('20220501', 'YYYYMMDD') THEN '출고대기'
               ELSE '출고미정' END AS "출고여부"
  FROM FOOD_ORDER 
 ORDER BY ORDER_ID ASC
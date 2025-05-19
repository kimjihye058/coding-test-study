SELECT     b.book_id
         , a.author_name
         , TO_CHAR(b.published_date, 'YYYY-MM-DD') AS published_date
FROM       book b
INNER JOIN author a ON b.author_id = a.author_id
WHERE      b.category = '경제'
ORDER BY   b.published_date ASC;
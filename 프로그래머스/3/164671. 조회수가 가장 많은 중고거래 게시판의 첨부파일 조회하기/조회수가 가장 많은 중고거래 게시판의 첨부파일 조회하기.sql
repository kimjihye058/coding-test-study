SELECT ('/home/grep/src/' || B.BOARD_ID || '/' || F.FILE_ID || F.file_name || F.file_ext) AS FILE_PATH
FROM USED_GOODS_BOARD B LEFT OUTER JOIN USED_GOODS_FILE F ON B.BOARD_ID = F.BOARD_ID
WHERE B.BOARD_ID = (
                    SELECT B.board_id
                    FROM (
                            SELECT *
                            FROM USED_GOODS_BOARD
                            ORDER BY views DESC
                         ) B
                    WHERE ROWNUM=1
                   )
ORDER BY F.FILE_ID DESC;
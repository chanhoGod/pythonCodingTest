-- 코드를 입력하세요
SELECT
a.FLAVOR
FROM (SELECT 
 FLAVOR,
 SUM(TOTAL_ORDER) as "PRICE"
 FROM FIRST_HALF 
 GROUP BY FLAVOR) as a
JOIN (SELECT 
 FLAVOR,
 SUM(TOTAL_ORDER) as "PRICE"
 FROM JULY 
 GROUP BY FLAVOR) as b ON a.FLAVOR = b.FLAVOR
Group by FLAVOR
ORDER by a.PRICE + b.PRICE desc
limit 3
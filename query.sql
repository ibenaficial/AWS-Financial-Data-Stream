SELECT name, substring(ts, 12, 2) as hour, max(high) as max_stock_price
FROM sta9760f2021benastream2
GROUP BY substring(ts, 12, 2), name
ORDER BY hour, name
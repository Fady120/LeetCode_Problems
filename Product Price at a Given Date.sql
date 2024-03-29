SELECT p1.product_id, COALESCE(price,10) AS price
FROM (SELECT 
      DISTINCT product_id 
      FROM Products) p1 
LEFT JOIN (SELECT 
           DISTINCT product_id,
           FIRST_VALUE(new_price) OVER(PARTITION BY product_id ORDER BY change_date DESC) AS price 
           FROM Products
           WHERE change_date <= "2019-08-16") p2 
ON p1.product_id = p2.product_id;
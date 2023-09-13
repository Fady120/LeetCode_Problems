# Write your MySQL query statement below

SELECT Sales.product_id, year AS first_year, quantity, price FROM Sales INNER JOIN Product ON Sales.product_id = Product.product_id 
WHERE (Sales.product_id, year) IN (
  SELECT product_id, MIN(year) FROM sales GROUP BY product_id 
);
-- Christopher Springer
-- 10/28/2026

USE northwind; 

-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a 
-- second query to find the name of the product that has that price. 

SELECT MIN(UnitPrice) AS 'Cheapest Price'
FROM products;

SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = 2.5;


-- 2. Write a query to find the average price of all items that Northwind sells. 
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help 
-- using the ROUND function to round the average price to the nearest cent.) 

SELECT ROUND(AVG(UnitPrice), 2) AS 'Average Price'
FROM products;


-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then 
-- write a second query to find the name of the product with that price, plus the name of 
-- the supplier for that product. 

SELECT MAX(UnitPrice) AS 'Most expensive price'
FROM products;

SELECT p.ProductName, p.UnitPrice, s.CompanyName
FROM products p
JOIN suppliers s
ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = 263.50;


-- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly 
-- salaries). 

SELECT SUM(salary) AS 'Total Monthly Payroll'
FROM employees;


-- 5. Write a query to identify the highest salary and the lowest salary amounts which any 
-- employee makes. (Just the amounts, not the specific employees!) 

SELECT MAX(salary) AS 'Highest Salary', MIN(salary) AS 'Lowest Salary'
FROM employees;


-- 6. Write a query to find the name and supplier ID of each supplier and the number of 
-- items they supply. Hint: Join is your friend here. 

SELECT s.CompanyName, s.SupplierID, COUNT(p.ProductID) AS 'Number of supplied items'
FROM suppliers s
JOIN products p
ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName, s.SupplierID;


-- 7. Write a query to find the list of all category names and the average price for items in 
-- each category. 

SELECT c.CategoryName, ROUND(AVG(p.UnitPrice), 2) as 'Average Price'
FROM categories c
JOIN products p
ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;


-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what 
-- is the name of each supplier and the number of items they supply. 

SELECT s.CompanyName, COUNT(p.ProductID) AS 'Number of items supplied'
FROM suppliers s
JOIN products p
ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5;


-- 9. Write a query to list products currently in inventory by the product id, product name, 
-- and inventory value (calculated by multiplying unit price by the number of units on 
-- hand). Sort the results in descending order by value. If two or more have the same 
-- value, order by product name. If a product is not in stock, leave it off the list. 

SELECT ProductID, ProductName, UnitPrice * UnitsInStock AS InventoryValue
FROM products
WHERE UnitsInStock != 0
ORDER BY InventoryValue DESC, ProductName;
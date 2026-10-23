/*
4	a) The name of the table that holds the items Northwind sells is products.
	b) The name of the table that holds the types/categories of the items Northwind sells
		is categories.
*/

USE northwind;
SELECT * FROM employees;
-- Margaret Peacock

SELECT * FROM products;
/*	a) My default was already set to Limit to 10 rows upon opening this query
	But if I wanted to change it, I would click the pulldown option in the 
    Query editor toolbar for the limiter.
    b) To write the query to limit the number of rows, you use LIMIT 0, #.
    I found this answer in the Output pane in the Action section when running the script.
*/

SELECT * FROM categories;
-- The category ID for seafood is 8.

SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders LIMIT 0, 50;



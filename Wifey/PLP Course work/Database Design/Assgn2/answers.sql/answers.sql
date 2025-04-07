-- Selecting checknumbers
SELECT checkNumber, paymentDate, amount
FROM payments;

-- Choosing from orders
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;

-- Employee list
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

-- Offices table
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;

-- Products table
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;



-- Naresh IT Ass-2 ( Data Manipulatin Basics )

-- 1. Data Insertion (Populating the customer registry)
INSERT INTO bank_customers (account_number, customer_name, customer_age, account_balance)
VALUES (1001, 'Krishna Kumar', 22, 5000.00);

INSERT INTO bank_customers (account_number, customer_name, customer_age, account_balance)
VALUES (1002, 'Rohan Sharma', 19, 1200.50);

-- Commit transaction to ensure data persistence in the backend
COMMIT;


-- 2. Data Retrieval (Basic Select and Filtering Queries)
-- View all records in the table
SELECT * FROM bank_customers;

-- Filter data using a specific condition (Account search)
SELECT customer_name, account_balance 
FROM bank_customers 
WHERE account_number = 1001;


-- 3. Data Modification (Simulating a balance update)
UPDATE bank_customers 
SET account_balance = account_balance + 500.00 
WHERE account_number = 1001;

COMMIT;


-- 4. Data Deletion (Removing a record safely via Primary Key)
DELETE FROM bank_customers 
WHERE account_number = 1002;

-- Final verification to review operational states
SELECT * FROM bank_customers;

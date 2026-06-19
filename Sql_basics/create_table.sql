-- NareshIT Classroom Lab Exercise
-- Purpose: Foundational syntax practice for DDL/DML statements.
-- Scope: Basic table creation.

CREATE TABLE Customer_data{
	acc_no NUMBER(12) PRIMARY_KEY,
	acch_name VARCHAR(20) NOT NULL,
	acc_bal NUMBER(10,2) CHECK (acc_bal >=0),
	customer_age NUMBER(3)
};
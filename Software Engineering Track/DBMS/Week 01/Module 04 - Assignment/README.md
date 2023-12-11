> # **```Assignment 1```**
>
> <summary>
> Create tables  
    - Make a student table  
    - Make a Library table  
    - Make a Fees table  
	Create table with proper relations.

</summary> 

```postgres
CREATE DATABASE assignment;

USE assignment;

-- #################
-- Q1
-- Foriegn key is responsible for establishing relation between tables
-- #################

CREATE TABLE Student
(
	Stu_ID INT PRIMARY KEY,
    Stu_Name VARCHAR(30),
    Address VARCHAR(255) NOT NULL DEFAULT 'Bangladesh',
    Mail VARCHAR(100),
    Age INT CHECK(Age > 10)
);

CREATE TABLE Library
(
	Lib_ID INT PRIMARY KEY,
    BookName VARCHAR(50),
    Stu_ID INT,
    Previous_book_lend INT,
    FOREIGN KEY(Stu_ID) REFERENCES Student(Stu_ID)
);

CREATE TABLE Fee 
(
	Fee_receipt_id INT PRIMARY KEY,
    Fee_amount FLOAT,
    Stu_ID INT,
    Is_fee_paid BOOL,
    FOREIGN KEY(Stu_ID) REFERENCES Student(Stu_ID)
);

DROP DATABASE assignment;

-- #################
-- Q2
-- Constraint identifies condition and abstain from false conditions
-- #################
CREATE TABLE Student
(
	Stu_ID INT PRIMARY KEY,
    Stu_Name VARCHAR(30),
    Address VARCHAR(255) NOT NULL DEFAULT 'Bangladesh',
    Mail VARCHAR(100),
    Age INT CHECK(Age > 10),
    CONSTRAINT mail_check UNIQUE(Mail)
);

CREATE TABLE Library
(
	Lib_ID INT PRIMARY KEY,
    BookName VARCHAR(50),
    Stu_ID INT,
    Previous_book_lend INT,
    FOREIGN KEY(Stu_ID) REFERENCES Student(Stu_ID),
    CONSTRAINT check_lended_book CHECK(Previous_book_lend <= 2)
);

CREATE TABLE Fee 
(
	Fee_receipt_id INT PRIMARY KEY,
    Fee_amount FLOAT,
    Stu_ID INT,
    Is_fee_paid BOOL,
    FOREIGN KEY(Stu_ID) REFERENCES Student(Stu_ID),
    CONSTRAINT check_fee_payment CHECK(Is_fee_paid = FALSE)
);
```
CREATE DATABASE assignment;

USE assignment;

-- #################

-- Q1

-- Foriegn key is responsible for establishing relation between tables

-- #################

CREATE TABLE
    Student (
        Stu_ID INT PRIMARY KEY,
        Stu_Name VARCHAR(30),
        Address VARCHAR(255) NOT NULL DEFAULT 'Bangladesh',
        Mail VARCHAR(100),
        Age INT CHECK(Age > 10)
    );

CREATE TABLE
    Library (
        Lib_ID INT PRIMARY KEY,
        BookName VARCHAR(50),
        Stu_ID INT,
        Previous_book_lend INT,
        FOREIGN KEY(Stu_ID) REFERENCES Student(Stu_ID)
    );

CREATE TABLE
    Fee (
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

CREATE TABLE
    Student (
        Stu_ID INT PRIMARY KEY,
        Stu_Name VARCHAR(30),
        Address VARCHAR(255) NOT NULL DEFAULT 'Bangladesh',
        Mail VARCHAR(100),
        Age INT CHECK(Age > 10),
        CONSTRAINT mail_check UNIQUE(Mail)
    );

CREATE TABLE
    Library (
        Lib_ID INT PRIMARY KEY,
        BookName VARCHAR(50),
        Stu_ID INT,
        Previous_book_lend INT,
        FOREIGN KEY(Stu_ID) REFERENCES Student(Stu_ID),
        CONSTRAINT check_lended_book CHECK(Previous_book_lend <= 2)
    );

CREATE TABLE
    Fee (
        Fee_receipt_id INT PRIMARY KEY,
        Fee_amount FLOAT,
        Stu_ID INT,
        Is_fee_paid BOOL,
        FOREIGN KEY(Stu_ID) REFERENCES Student(Stu_ID),
        CONSTRAINT check_fee_payment CHECK(Is_fee_paid = FALSE)
    );

-- #################

-- Q5 to Q10

-- #################

CREATE TABLE
    Employee (
        EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
        FirstName VARCHAR(100),
        LastName VARCHAR(100),
        Age INT,
        Department VARCHAR(100)
    );

INSERT INTO
    Employee (
        FirstName,
        LastName,
        Age,
        Department
    )
VALUES ('John', 'Doe', 28, 'Sales'), (
        'Jane',
        'Smith',
        32,
        'Marketing'
    ), (
        'Michael',
        'Johnson',
        35,
        'Finance'
    ), ('Sarah', 'Brown', 30, 'HR'), (
        'William',
        'Davis',
        25,
        'Engineering'
    ), ('Emily', 'Wilson', 28, 'Sales'), (
        'Robert',
        'Lee',
        33,
        'Marketing'
    ), ('Laura', 'Hall', 29, 'Finance'), ('Thomas', 'White', 31, 'HR'), (
        'Olivia',
        'Clark',
        27,
        'Engineering'
    );

-- Q5

SELECT DISTINCT Department FROM Employee;

-- Q6

SELECT LastName FROM Employee ORDER BY Age DESC;

-- Q7

SELECT LastName FROM Employee WHERE Age > 30;

-- Q8

SELECT * FROM Employee;

-- Q9

SELECT *
FROM Employee
WHERE
    FirstName LIKE "%son%"
    OR LastName LIKE "%son%";

-- Q10

SELECT * FROM Employee WHERE Department = "Engineering";
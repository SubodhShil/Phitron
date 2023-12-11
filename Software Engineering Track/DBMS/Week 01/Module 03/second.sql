CREATE DATABASE M3;

USE M3;

CREATE TABLE Student
(
    Roll CHAR(4) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(30) UNIQUE,
    Address VARCHAR(255) NOT NULL DEFAULT 'Bangladesh',
    Age INT CHECK(Age > 10)
);

DROP TABLE Student;

CREATE TABLE Library
(
	BookName VARCHAR(50) PRIMARY KEY,
    Library_roll CHAR(4),
    FOREIGN KEY (Library_roll) REFERENCES Student(Roll)
);

INSERT INTO Student (Roll, Name, Email, Address, Age) VALUES('0001', 'Roktim', 'rokto@gmail.ocm', 'Kaliapur', 11);


-- Alternative way to write (this is good for debugging, and condition checking)
CREATE TABLE Employee
(
	ID CHAR(4),
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(30) NOT NULL,
    Address VARCHAR(255) DEFAULT 'Bangladesh' NOT NULL,
    Age INT,

	-- Constraint rules  
    CONSTRAINT pk_rule PRIMARY KEY(ID),
    CONSTRAINT checking_rule CHECK(Age>18)
);

-- Composite primary key
CREATE TABLE Course
(
	CourseName VARCHAR(10),
    University VARCHAR(100),
    Credit INT,
    
    -- Constraints
    CONSTRAINT composite_primary_keys PRIMARY KEY (CourseName, University)
);

INSERT INTO Course(CourseName, University, Credit) VALUES ("CSE-101", "DU", 4);
INSERT INTO Course(CourscourseeName, University, Credit) VALUES ("CSE-101", "SMUCT", 3);


-- SELECT Query: to show data from table
-- Syntax: SELECT field1, field2,... FROM table_name;
SELECT University, Credit FROM Course; 

-- To see all field column
SELECT * FROM Course;

-- WHERE Query:
SELECT Credit FROM Course WHERE Credit>3;

-- Marks table
CREATE TABLE Marks 
(
    Roll INT PRIMARY KEY,
    CSE FLOAT NOT NULL DEFAULT 0,
    ME FLOAT NOT NULL DEFAULT 0,
    ENG FLOAT NOT NULL DEFAULT 0
);

INSERT INTO Marks(Roll, CSE, ME, ENG) VALUES(102, 90.5, 78, 85);
INSERT INTO Marks(Roll, CSE, ME, ENG) VALUES(101, 88, 85, 90);
INSERT INTO Marks(Roll, CSE, ME, ENG) VALUES(55, 99, 75, 66);

-- Arithmatic operation
SELECT CSE + ME + ENG
FROM Marks 
WHERE Roll=102;

-- Comparison operator
SELECT CSE, ME
FROM Marks
WHERE CSE > 50;


DROP DATABASE M3;

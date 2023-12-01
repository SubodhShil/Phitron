-- To create a database 
CREATE DATABASE db_name;

-- The query let us use an existing table from the database
USE test;

-- Query for creating a new table in the database
CREATE TABLE
    Students(
        Roll CHAR(4) PRIMARY KEY, -- Primary key is the unique  identifier 
        Name VARCHAR(50),
        Marks DOUBLE
    );

-- Insert field values

-- Way 01
INSERT INTO Students 
(`Roll`, `Name`, `Marks`) VALUES(33, 'Subodh', 77);

-- Way 02
INSERT INTO Students VALUES(1, "Roktim", 99);

-- Updating value
-- While updating values one should turn off the safe mode
SET SQL_SAFE_UPDATES = 0;

UPDATE students
SET Name = 'Roktim'
WHERE `Roll` = 1;

-- After updating the values safe mode should turn on
SET SQL_SAFE_UPDATES = 1;

-- Query for deleting an existing TABLE
DROP TABLE Students;

-- Delete values
DELETE FROM students
WHERE `Roll` = 1;

-- Show all available tables
SHOW TABLES;

-- To see the table structure
DESCRIBE Students;
-- or 
EXPLAIN Students;

-- To display a specific table
SELECT * FROM students;
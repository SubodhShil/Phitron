## CREATE TABLE Constraints

> With the use of constraints we can implement multiple rules. For example,   
NID has two constraints,  
**i.** NID has to be unique  
**ii.** It has to be the PRIMARY KEY of the table

Here are some constraints:
1. **PRIMARY KEY**: Unique identifier of a table. PRIMARY KEY is unique.
2. **FOREIGN KEY**: A field that is used as a PRIMARY KEY of another table of a database.
3. **UNIQUE**: Data that can't be repeatable through a particular table field.
4. **CHECK**
5. **DEFAULT**: What value a field cell should obtain if there is no input from user.
6. **NOT NULL**: If there is no DEFAULT value for a field cell then it will set the value NULL by the database itself. But if you don't want a null value than NOT NULL constraint can be use hereby.

<!-- Follow up questions -->

## SELECT Query
The query used for showing data. 

## WHERE Query
WHERE অনেকটা condition এর মতো কাজ করে, এটা নির্দিষ্ট কারো জন্য data দেখাতে ব্যবহার হয় । 

## Comparison Operators
1. =
2. < 
3. \>
4. <=
5. \>=
6. !=, <>

## Logical operator
Age 30 এর কম কিন্তু salary 12000 এর বেশি, তার name, salary বের করো । 

```sql
SELECT Name, Salary
FROM Employee
WHERE Age < 30 AND SALARY > 12000;
```

## DISTINCT, ORDER BY, LIMIT, OFFSET
1. **DISTINCT**: This query only shows the distinct or unique data.
   ```sql
    SELECT DISTINCT Country 
    FROM Suppliers
    WHERE SupplierID > 10 and SupplierID < 20;
   ```
2. **ORDER BY**: To sort data in ascending or descending order. 
3. **LIMIT**: Limits the data to be shown. LIMIT মানে কতগুলো data দেখাতে হবে ।  
4. **OFFSET**: OFFSET বলতে কতগুলো data বাদ গেলো সেটা । 

## Sequential order 
```postgres
SELECT
FROM 
WHERE 
ORDER BY 
LIMIT 
OFFSET
```
Query লেখার সময় সবসময় এই order টা maintain করতে হবে, ধরা যাক তুমি OFFSET query লিখতে চাচ্ছো সেক্ষেত্রে OFFSET আগে উপরের query গুলোও লিখতে হবে । 

## IN, NOT IN, LIKE, AS

```sql
WHERE Roll = 102
   OR Roll = 104 
   OR Roll = 106 

-- Better way to write the same query
WHERE Roll IN (102, 104, 106)
```

### LIKE
Suppose you have such data
```sql 
ANA MONA
ANA ANTHONY
RAPID KARIM
ANA SIKDER
LAILI ANA
```
Now you want to select all the names having 'ANA', to do this you can write query like this: 
```sql
WHERE Name = 'ANA'
WHERE Name LIKE '%ANA%'
```

### AS
AS represent alias of a particular field or multiple field name.


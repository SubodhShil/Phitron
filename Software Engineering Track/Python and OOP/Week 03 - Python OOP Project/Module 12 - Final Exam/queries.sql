USE bankDB;

CREATE TABLE
    users (
        account_number VARCHAR(200) PRIMARY KEY,
        name varchar(50),
        password varchar(50),
        email varchar(50),
        Account_type varchar(100),
        address varchar(150)
    );
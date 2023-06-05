create database loginsystem;

Create table login ( 
    name varchar(30),
    password varchar(30),
    epost varchar(30), 
);

CREATE TABLE gamepoints (
    name varchar(30),
    score INT CHECK (score >= 0 AND score <= 100)
);

ALTER table passwd
ADD new_column_name VARCHAR(30);

SELECT * FROM information_schema.processlist WHERE db = 'your_database_name';

RENAME DATABASE current_database_name TO new_database_name;


insert into login (name,password,epost) values("felix","123","jobb@nå.com");

ALTER TABLE login MODIFY COLUMN passwd VARCHAR(64);

select * from login username;

DELETE FROM login;

desc table_name;

CREATE USER 'FelixAdmin'@'localhost' IDENTIFIED BY 'FelixAdmin';
GRANT ALL PRIVILEGES ON loginsystem.* TO 'FelixAdmin'@'localhost';

FLUSH PRIVILEGES;

SHOW GRANTS FOR 'FelixAdmin'@'localhost';

DROP USER 'FelixAdmin'@'localhost';
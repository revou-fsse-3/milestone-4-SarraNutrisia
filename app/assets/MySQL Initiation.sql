create database Banking_Management;

use Banking_Management;

create table users(
id INTEGER auto_increment primary key,
username VARCHAR(255) unique,
email VARCHAR(255) unique,
password_hash VARCHAR(255),
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp
);

create table accounts(
id INTEGER auto_increment primary key,
user_id INTEGER, foreign key (user_id) references users (id),
account_type VARCHAR(255),
account_number VARCHAR(255) unique,
balance DECIMAL(10,2),
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp
);

create table transactions(
id INTEGER auto_increment primary key,
from_account_id INTEGER, foreign key (from_account_id) references accounts (id),
to_account_id INTEGER, foreign key (to_account_id) references accounts (id),
amount DECIMAL(10,2),
type VARCHAR(255),
description VARCHAR(255),
created_at timestamp default current_timestamp
);

SELECT *
FROM users;

SELECT *
FROM accounts;

SELECT *
FROM transactions;


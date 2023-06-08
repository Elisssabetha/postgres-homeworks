-- SQL-команды для создания таблиц
CREATE TABLE customers
(
customer_id varchar(5) PRIMARY KEY,
company_name varchar(200) UNIQUE,
contact_name varchar(100)
);

CREATE TABLE IF NOT EXISTS employees
(
employee_id int PRIMARY KEY,
first_name 	varchar(50),
last_name 	varchar(50),
title varchar(50),
birth_date date,
notes text
);

CREATE TABLE IF NOT EXISTS orders
(
order_id int PRIMARY KEY,
customer_id varchar(5) REFERENCES customers(customer_id) ON DELETE CASCADE,
employee_id int REFERENCES employees(employee_id) ON DELETE CASCADE,
order_date date,
ship_city varchar(30)
)

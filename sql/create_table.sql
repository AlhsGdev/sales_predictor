CREATE DATABASE salesdb;

USE salesdb;

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_number VARCHAR(50),
    sales FLOAT,
    quantity_ordered INT,
    price_each FLOAT,
    order_date DATE
);
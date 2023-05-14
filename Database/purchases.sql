CREATE TABLE purchases (
purchase_id int auto_increment primary key,
item_name varchar(255),
quantity int,
price decimal(10,2),
customer_name varchar(255),
customer_phone varchar(255),
purchase_date date,
purchase_time time
);

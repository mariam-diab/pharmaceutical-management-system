CREATE TABLE purchases (
purchase_id int not null auto_increment primary key,
customer_name varchar(255) not null,
purchase_date date not null,
purchase_time time not null,
item_name varchar(255) not null,
quantity int not null,
price decimal(10,2) not null,
total decimal(10,2) not null
);

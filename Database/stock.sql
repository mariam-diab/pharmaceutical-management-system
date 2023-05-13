CREATE TABLE stock (
item_id int not null auto_increment primary key,
item_name varchar(255) not null,
provider_name varchar(255) not null,
quantity int not null,
price decimal(10,2) not null,
expire_date date not null
);

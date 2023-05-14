CREATE TABLE stock (
  item_id int auto_increment primary key,
  item_name varchar(255),
  provider_name varchar(255),
  quantity int,
  expire_date date,
  price int default 30
);

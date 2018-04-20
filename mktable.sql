DROP TABLE cust_order;
DROP TABLE product;
DROP TABLE order_line;
CREATE TABLE product(
 id VARCHAR(6) PRIMARY KEY,
 description VARCHAR(100),
 price DECIMAL(10,2)
);

insert into product values('112233','Laptop Computer , Yoga 910',1300);

insert into product values('112234','Large Screen Monitor',100);

CREATE TABLE cust_order(
	id int PRIMARY KEY,
	status VARCHAR(10)
);
insert into cust_order values(101,'incomplete');--Customer is adding to this
insert into cust_order values(102,'waiting');--Customer is adding to this
insert into cust_order values(103,'waiting');--Customer is adding to this
insert into cust_order values(104,'processing');
insert into cust_order values(105,'ready');
insert into cust_order values(106,'complete');

CREATE TABLE order_line(
	cust_order int,
	product int,
	qty int,
	PRIMARY KEY (cust_order,product),
	FOREIGN KEY(cust_order) REFERENCES cust_order(id),
	FOREIGN KEY(product) REFERENCES product(id) 
);
insert into order_line values(105,112233,1);
insert into order_line values(105,112234,1);







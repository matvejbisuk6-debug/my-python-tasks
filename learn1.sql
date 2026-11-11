
DROP TABLE IF EXISTS "public".orders;
DROP TABLE IF EXISTS "public".products;

CREATE TABLE "public".products(
id SERIAL PRIMARY KEY,
product_name VARCHAR(50) NOT NULL,
price NUMERIC(10, 2) NOT NULL,
quantity INT DEFAULT 0
);

INSERT INTO "public".products(id, product_name, price, quantity) VALUES
(1, 'Телефон', 50000, 5),
(2, 'Персональный компьютер', 100000, 2),
(3, 'Наушники', 5000, 10);

CREATE TABLE "public".orders(
id SERIAL PRIMARY KEY,
order_identifier VARCHAR(50) NOT NULL,
order_date VARCHAR(50) NOT NULL,
status VARCHAR DEFAULT 'New'
);

INSERT INTO "public".orders(id, order_identifier, order_date, status) VALUES
(1, 1, '20.05.2026', 'New'),
(2, 2, '05.09.2013', 'old'),
(3, 3, '13.12.2004', 'oldest');

SELECT
orders.id AS order_id,
orders.order_date,
products.product_name,
products.price
FROM "public".orders
INNER JOIN "public".products
    ON orders.order_identifier = CAST(products.id AS VARCHAR);

SELECT
orders.status,
COUNT(orders.id) AS orders_count,
SUM(products.price) AS total_revenue,
ROUND(AVG(products.price), 2) AS average_price
FROM "public".orders
INNER JOIN "public".products
    ON orders.order_identifier = CAST(products.id AS VARCHAR)
GROUP BY orders.status;

SELECT
orders.id AS order_id,
products.product_name,
products.price,
products.quantity,
products.price * products.quantity AS total_stock_sum,
products.price * 0.85 AS total_stock_sum,
products.price + 500 AS total_stock_sum
FROM "public".orders
INNER JOIN "public".products
     ON orders.order_identifier = CAST(products.id AS VARCHAR);
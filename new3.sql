DROP TABLE IF EXISTS "public".orders;
DROP TABLE IF EXISTS "public".users;

CREATE TABLE "public".users (
id INT PRIMARY KEY,
username VARCHAR(50) NOT NULL,
city VARCHAR(100) UNIQUE
);

INSERT INTO "public".users(id, username, city) values
(1, 'Алексей', 'Екатеринбург'),
(2, 'Матвей', 'Переславль-Залесский'),
(3, 'Екатерина', 'Великий Новгород');

CREATE TABLE "public".orders (
id INT PRIMARY KEY,
user_id INT REFERENCES "public".users(id),
amount NUMERIC(10, 2),
status VARCHAR(100)
)

INSERT INTO "public".orders (id, user_id, amount, status) values
(1, 1, 1500.00, 'paid'),
(2, 1, 2300.50, 'no paid'),
(3, 2, 500.00, 'paid'),
(4, 2, 1200.00, 'no paid'),
(5, 3, 3400.00, 'paid'),
(6, 3, 890.00, 'no paid');

SELECT * FROM "public".users u
JOIN "public".orders o ON u.id = o.user_id AND o.status = 'paid';

SELECT
u.username,
COALESCE(SUM(o.amount), 0) AS total_paid
FROM "public".users u
LEFT JOIN "public".orders o ON o.user_id = u.id AND o.status = 'paid'
GROUP BY u.id, u.username
ORDER BY total_paid DESC;
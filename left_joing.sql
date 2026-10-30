CREATE TABLE "public".users (
     id BIGINT NOT NULL PRIMARY KEY,
     first_name VARCHAR(64) NOT NULL,
     last_name VARCHAR(64) NOT NULL,
     email VARCHAR(128) NOT NULL
);

INSERT INTO "public".users(id, first_name, last_name, email) values
(1, 'Алексей', 'Смирнов', 'lexa@email.com'),
(2, 'Мария', 'Федорова', 'Masha@email.com'),
(3, 'Михаил', 'Александров', 'Micha@email.com');

SELECT
      c.developer_name AS dev_name,
      c.developer_work AS job,
      u.email AS user_email
FROM "public".countries c
LEFT JOIN "public".users u ON C.id = u.id;

SELECT
     u.first_name AS user_name,
     c.country_name AS country
FROM "public".users u
LEFT JOIN "public".countries c ON u.id = c.id;
      
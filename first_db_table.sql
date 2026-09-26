CREATE TABLE "public".users (
id BIGINT NOT NULL PRIMARY KEY,
first_name VARCHAR(64) NOT NULL,
last_name VARCHAR(64) NOT NULL,
email VARCHAR(128) NOT NULL
);

INSERT INTO "public".users (id, first_name, last_name, email) values
(1, 'Алексей', 'Смирнов', 'lexa@email.com'),
(2, 'Мария', 'Федорова', 'Masha@email.com'),
(3, 'Михаил', 'Александров', 'Micha@email.com');
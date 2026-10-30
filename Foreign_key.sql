CREATE TABLE "public".users (
    id BIGINT PRIMARY KEY,
    first_name VARCHAR(64) NOT NULL,
    country_id INT,

    FOREIGN KEY (country_id) REFERENCES "public".countries(id)
);
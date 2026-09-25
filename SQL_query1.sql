SELECT * FROM "public".countries;
SELECT * FROM "public".countries WHERE developer_work = 'QA тестировщик';
SELECT developer_name, capital FROM "public".countries;
SELECT * FROM "public".countries ORDER BY country_name ASC;
SELECT * FROM "public".countries ORDER BY country_name DESC;
SELECT * FROM "public".countries WHERE country_name != 'Россия';
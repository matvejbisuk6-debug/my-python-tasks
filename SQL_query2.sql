SELECT COUNT(*) FROM "public".countries;
SELECT developer_work, COUNT (*) FROM "public".countries GROUP BY developer_work;
SELECT developer_work, COUNT (*) FROM "public".countries WHERE developer_work IN ('QA тестировщик', 'Бэкэнд разработчик')GROUP BY developer_work;
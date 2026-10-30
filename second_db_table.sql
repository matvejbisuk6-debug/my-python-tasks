CREATE TABLE "public".countries(
id BIGINT NOT NULL PRIMARY KEY,
country_name VARCHAR(100) NOT NULL,
capital VARCHAR(100) NOT NULL,
developer_name VARCHAR(1000) NOT NULL,
developer_work VARCHAR(1000) NOT NULL
);

INSERT INTO "public".countries(id, country_name, capital, developer_name, developer_work) values
(1, 'Россия', 'Москва', 'Иван', 'бэкэнд разработчик')
(2, 'США', 'Вашингтон', 'Мэри', 'Проджект менеджер')
(3, 'Франция', 'Париж', 'Луи', 'фронтенд разработчик')
(4, 'Польша', 'Варшава', 'Станислава', 'QA тестировщик')
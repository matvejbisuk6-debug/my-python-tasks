salary INT DEFAULT 18,
user_id INT,
FOREIGN KEY (user_id) REFERENCES public.users(id)
);

CREATE TABLE "public".residents (
id SERIAL PRIMARY KEY,
name_town VARCHAR (50) NOT NULL,
region VARCHAR (100),
auto_code INT DEFAULT 18
);

INSERT INTO "public".users(name_user, salary, user_id) VALUES
('Елена', '30000', 1),
('Александр', '50000', 2),
('Виктория', '40000', 3),
('Сергей', '60000', 4)

INSERT INTO "public".residents(name_town, region, auto_code) VALUES
('Любим', 'Ярославская Область', '76'),
('Пошехонье', 'Ярославская Область', '76'),
('Белозерск', 'Вологодская Область', '35'),
('Мезень', 'Архангельская Область', '29'),
('Красный Холм', 'Тверская Область', '69');

SELECT * FROM public.users;

SELECT u.user_name, r.name_town
FROM public.users u
JOIN public.residents r ON r.user_id = u.id;

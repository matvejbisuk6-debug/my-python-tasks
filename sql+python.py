import psycopg

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Motya_0212",
    "host": "localhost",
    "port": "5432"
}

try:
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:

            sql_query = """
               SELECT u.name_user, r.name_town
               FROM public.users u
               JOIN public.residents r ON r.user_id = u.id;
            """

            cursor.execute(sql_query)
            rows = cursor.fetchall()

            print("---Список жителей и их городов---")
            for row in rows:
                print(f"Житель: {row[0]:<12} | Город{row[1]}")

except Exception as error:
    print(f"Произошла ошибка при работе с PostgreeSQL: {error}")
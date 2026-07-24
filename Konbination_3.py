#Задача 1
every_day = [+0.10, -0.05, +0.12]

def manage_wallet(target_profit):
    balance = 1000
    while balance < target_profit and balance > 100:
        for i in every_day:
            balance = balance + (balance * i)
        if i < 0:
            print("Предупреждение")
    print(f"Итоговый баланс равен: {balance}")
manage_wallet(2000)


#Задача 2
password = "Akidh_9"

def check_password(password):
    if len(password) >= 8:
        has_upper = any(i.isupper() for i in password)
        has_number = any(i.isdigit() for i in password)
        has_letter = any(i.islower() for i in password)
        if has_upper == True and has_number == True and has_letter == True:
            return "Надежный"
        else:
            return "Ненадежный"
    return "Ненадежный"
print(check_password(password))

#Задача 3
amount = 200
active = "deposite"

def atm_transaction(action, amount):
    balance = 1000
    if action == "deposite":
        balance *= amount
        return balance
    elif action == "withdraw":
        balance -= amount
        return balance
    else:
        print("Предупреждение")
    return balance
print(atm_transaction(active, amount))

#Задача 4
temperature_list = [75, 105, 150]
max_limit = 130

def analyze_temperatures(temp_list, max_limit):
    counter = 0
    average = sum(temp_list) // len(temp_list)
    for i in temp_list:
        if i == 999:
            break
        if i > max_limit:
            counter += 1
    print(f"Средняя температура - {average}, датчик превысил критическую отметку - {counter} раз")
analyze_temperatures(temperature_list, max_limit)

#Задача 5
secret_number = 99
max_attempts = 10

def start_game(secret_number, max_attempts):
    attempts = 0
    while attempts < max_attempts:
        number = int(input("Введите число: "))
        attempts += 1
        if number < secret_number:
            print("Меньше")
        elif number > secret_number:
            print("Больше")
        elif number == secret_number:
            return True
        elif max_attempts == attempts:
            return False
start_game(secret_number, max_attempts)


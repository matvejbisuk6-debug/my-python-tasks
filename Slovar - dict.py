#Задача 1
sentence = "Девочка учится просто так"

def newest_sentence(new_sentence):
    new_sentence = new_sentence.lower()
    new_sentence = new_sentence.replace(" ", "")
    my_dict = {}
    for i in new_sentence:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict
print(newest_sentence(sentence))

#Задача 2
basket_of_product1 = {"Хлеб": 1, "Вода": 2, "Молоко": 1}
basket_of_product2 = {"Молоко": 1, "Творог": 2, "Чай": 1}

def new_basket_of_product(products1, products2):
    for i in products2:
        if i in products1:
            products1[i] += products2[i]
        else:
            products1[i] = products2[i]
    return products1
print(new_basket_of_product(basket_of_product1, basket_of_product2))

#Задача 3
synonims = {"большой": ["огромный", "крупный"], "красивый": ["прекрасный"]}

def new_synonims(new_words):
    result = {}
    for key, value_list in new_words.items():
        for i in value_list:
            result[i] = key
    return result
print(new_synonims(synonims))

#Задача 4
company = {
    "разработка": {"Иванов": 120000, "Петров": 150000},
    "маркетинг": {"Сидоров": 90000, "Кузнецова": 110000}
}

def new_company(work):
    max_avg = 0
    best_dep = ("")
    for key, value_dict in work.items():
        current_salaries = value_dict.values()
        avg_salary = sum(current_salaries) / len(current_salaries)
        if avg_salary > max_avg:
            max_avg = avg_salary
            best_dep = key
    return best_dep
print(new_company(company))

#Задача 5
exchange_rate = {"USD": 92.5, "EUR": 101.2, "CNY": 12.8}
investor_assets = [{"валюта": "USD", "количество": 500}, {"валюта": "CNY", "количество": 3000}]

def total_value_of_assets(axchange, assets):
    counter = 0
    for asset in assets:
        currency = asset["валюта"]
        amount = asset["количество"]
        rate = axchange[currency]

        counter += amount * rate
        return counter
print(total_value_of_assets(exchange_rate, investor_assets))
#Задача 1
shop_A = {"яблоки": 100, "бананы": 80, "груши": 150}
shop_B = {"яблоки": 95, "сливы": 120, "груши": 160}

def shopping(shop1, shop2):
    new_shop = shop1.copy()
    for i in shop2:
        if i in new_shop:
           new_shop[i] = min(new_shop[i], shop2[i])
        else:
            new_shop[i] = shop2[i]
    return new_shop
print(shopping(shop_A, shop_B))

#Задача 2
list_of_grades = [("Анна", 4), ("Игорь", 3), ("Анна", 5), ("Игорь", 2), ("Матвей", 3), ("Матвей", 4)]

def raiting_log(grades):
    log = {}
    for name, grade in grades:
        if name in log:
            log[name] = max(log[name], grade)
        else:
            log[name] = grade
        return log
print(raiting_log(list_of_grades))

#Задача 3
text = "Питон - отличный язык. Язык Питон прост и понятен!"

def new_text(sentence):
    new_sentence = {}
    sentence = sentence.lower()
    sentence = sentence.replace(",", "")
    sentence = sentence.replace(".", "")
    sentence = sentence.replace("!", "")
    sentence = sentence.replace("-", "")
    words = sentence.split()
    for word in words:
        if word in new_sentence:
            new_sentence[word] += 1
        else:
            new_sentence[word] = 1
    return new_sentence
print(new_text(text))

#Задача 4
like_colors = {"Олег": "красный", "Маша": "синий", "Аня": "красный", "Иван": "зеленый"}

def new_colors(colors):
    common_colors = {}
    for key,value in colors.items():
        if value in common_colors:
            common_colors[value].append(key)
        else:
            common_colors[value] = [key]
    return common_colors
print(new_colors(like_colors))

#Зажача 5
word = input("Введите слово: ")

def count_chars(s):
    char_count = {}
    for i in s:
        if i in char_count:
           char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count
print(count_chars(word))

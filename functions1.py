#Задача 1
user_num = int(input("Введите число: "))

def square_number(x):
    return x ** 2
print(square_number(user_num))

#Задача 2
num = int(input("Введите число : "))

def is_even(number):
    if number % 2 == 0:
        return True
    if number % 2 == 1:
        return False
print(is_even(num))

#Задача 3
mark = [4, 5, 3, 5]

def calculate_average(marks):
    return  sum(marks) / len(marks)
print(calculate_average(mark))

#Задача 4
new_list = [-3, 4, -15, 22, 0]

def filter_positive(numbers):
    my_list = []
    for num in numbers:
        if num > 0:
            my_list.append(num)
        return my_list
print(filter_positive(new_list))

#Задача 5
words_list = ["Привет", "Пока", "Нет", "Прощай"]

def analyze_words(word_list):
    counter = 0
    for word in word_list:
        if len(word) > 4:
            counter += 1
        return counter
print(analyze_words(words_list))
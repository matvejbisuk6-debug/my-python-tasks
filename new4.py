#Задача 1
def calculate_delivery(distance):
    if distance <= 10:
        return "Базовая цена 200 рублей"
    elif 10 < distance <= 50:
        return "Базовая цена = 200 рублей"
    else:
        return "Базовая цена 700 рублей"

print(calculate_delivery(100))

#Задача 2
while True:
    log_lines = ["INFO: User logged in", "ERROR: Connection failed", "INFO: Retry success", "CRITICAL: Database down", "ERROR: Tail error"]
    line = "ERROR: Connection failed"
    if line in log_lines:
        log_lines.pop(3)
        log_lines.sort()
        print("Элемент удален:", log_lines)
        break

#Задача 3
class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = [5, 4, 3, 2]

    def add_grade(self, grade):
        if grade < 6 and grade > 0:
            self.__grades.append(grade)
            return f"Ученик {self.name} получил оценку {grade}, его оценки -- {self.__grades}"
        else:
            return "Ошибка, оценка не добавлена"

    def get_average(self):
        avarage = sum(self.__grades) / len(self.__grades)
        return f"Средний бал ученика {self.name} равен {avarage}"

student = Student("Матвей")
print(student.add_grade(5))
print(student.get_average())

#Задача 4

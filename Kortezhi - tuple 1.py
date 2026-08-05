#Задача 1
new_tuple = (1, 3, 5, 8)

def is_monotonic(t):
    for i in range(len(t) - 1):
        if t[i + 1] <= t[i]:
            return False
    return True
print(is_monotonic(new_tuple))

#Задача 2
tuple_1 = (1, 2)
tuple_2 = (3, 4, 2)

def merge_and_find(t1, t2, element):
    new_tuple2 = t1 + t2
    for element in new_tuple2:
        if element not in new_tuple2:
            return -1
    return new_tuple2.index(element)
print(merge_and_find(tuple_1, tuple_2, 2))

#Задача 3
tuple_1 = (2, 4, 3, 5, 7, 8, 9)
target = 11

def find_pairs_win_sum(t, target):
    result_tuple = ()
    seen = set()
    for i in t:
        j = target - i
        result_tuple += ((i, j), )
        seen.add(i)
    return result_tuple
print(find_pairs_win_sum(tuple_1, target))

#Задача 4
first = ("a", "a", "b", "b", "b", "a")

def compress_tuple(t):
    seen1 = set()
    new_tuple = ()
    counter = 0
    for i in t:
        if i not in seen1:
            counter = t.counter(i)
            new_tuple += ((i, counter), )
            seen1.add(i)
    return new_tuple
print(compress_tuple(first))

#Задача 5
secons = ((1, 2, 3), (4, 5, 6))

def transpose_matrix(matrix):
    return tuple(zip(*matrix))
print(transpose_matrix(secons))
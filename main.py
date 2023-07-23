import random
# Завдання 1
#
# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
####################################################################################

# random_list_of_integers = []                                                        # генерация списка
# for i in range(10):
#     random_list_of_integers.append(random.randint(1, 10))
#
# print(random_list_of_integers)
#
#
# def mult_elements(some_list_of_integers):                                           # функция умножения целых
#     mult_of_numbers = 1
#     for i in some_list_of_integers:
#         mult_of_numbers *= i
#     return print(f"Multiplication of all numbers in the list = {mult_of_numbers}")
#
#
# mult_elements(random_list_of_integers)

####################################################################################
# Завдання 2
#
# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
####################################################################################

# random_list_of_integers = []                                                        # генерация списка
# for i in range(10):
#     random_list_of_integers.append(random.randint(-10, 10))
#
# print(random_list_of_integers)
#
#
# def find_min(some_list_of_integers):                                                # функция нахождения минимального числа
#     return print(f"Minimum number from the list = {min(some_list_of_integers)}")
#
#
# find_min(random_list_of_integers)

####################################################################################
# Завдання 3
#
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
####################################################################################

# random_list_of_integers = []                                                        # генерация списка
# for i in range(10):
#     random_list_of_integers.append(random.randint(1, 100))
#
#
# def simple_num(some_list_of_integers):                                              # функция нахождения количества простых чисел
#     list_simpl = []
#
#     for i in some_list_of_integers:
#         if i > 1:
#             is_simple = True
#             for j in range(2, i):
#                 if i % j == 0:
#                     is_simple = False
#                     break
#             if is_simple:
#                 list_simpl.append(i)
#     return print(f"List of integers {random_list_of_integers}" + "\n" + f"List of prime numbers {list_simpl}" + "\n" + f"There are only {len(list_simpl)} prime numbers")
#
#
# simple_num(random_list_of_integers)

####################################################################################
# Завдання 4
#
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.
# ###################################################################################

# random_list_of_integers = []                                                        # генерация списка
# for i in range(10):
#     random_list_of_integers.append(random.randint(1, 10))
#
# print(random_list_of_integers)
# delete_number = int(input("Enter the number you want to delete: "))
#
#
# def delete_int(some_list_of_integers, some_number):
#     counter = some_list_of_integers.count(some_number)
#     for i in range(counter):
#         some_list_of_integers.remove(some_number)
#
#     return print(f"Corrected list of numbers {random_list_of_integers}" + "\n" + f"Number of deleted numbers: {counter}")
#
#
# delete_int(random_list_of_integers, delete_number)

####################################################################################
# Завдання 5
#
# Напишіть функцію, яка отримує два списки як параметр і повертає список,
# що містить елементи обох списків.
####################################################################################

# list_fruits_1 = ["apple", "orange", "banana"]
# list_fruits_2 = ["peach", "pear", "pineapple"]
#
#
# def mixed_list(list_1, list_2):
#     list_1.extend(list_2)
#     return print(f"Mixed list {list_1}")
#
#
# mixed_list(list_fruits_1, list_fruits_2)

####################################################################################
# Завдання 6
#
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.
# ###################################################################################



####################################################################################
# 1. Напишите программу, которая запрашивает у пользователя целые числа по одному (ввод с клавиатуры) до тех пор,
# пока не будет введен 0.
# Программа должна вывести сумму всех введенных положительных чисел (0 не учитывать).
# Sum = 0
#
# while True:
#     number = int(input("enter one number: "))
#     if number == 0:
#         print(f"you got sum of {Sum}")
#         break
#     else:
#         Sum += number
import random

# 2. Пользователь вводит натуральное число n (> 0).
# Найдите и выведите наибольшую цифру в его десятичной записи.
# number = int(input("enter number: "))
# max_digit = 0
#
# if number <= 0:
#     print("некорректное число. Введите натуральное число n (> 0).")
# else:
#     while number > 0:
#         current_digit = number % 10
#
#         if current_digit > max_digit:
#             max_digit = current_digit
#
#         number //= 10
#
# print(max_digit)


# 3. Даны положительные числа A и B (A > B).
# На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
# Не используя операции умножения и деления, найти длину незанятой части отрезка A.
# number_1 = int(input("enter first number: "))
# number_2 = int(input("enter second number: "))
#
# if number_1 <= 0 or number_1 <= 0:
#     print("Error: first and second must be positive")
# else:
#     current_1 = number_1
#     count_2 = 0
#     print(f"Start lengthen of first number: {number_1}, lengthen of second number: {number_2}")
#
#     while current_1 >= number_2:
#         current_1 = current_1 - number_2
#         count_2 += 1
#         print(f"placed cut of second number {count_2}. left lengthen: {current_1}")
#
#     # 3. Результат
#     print(f"max cuts of second number: {count_2}")
#     print(current_1)


# 4. Дано целое число N (> 0).
# С помощью операций деления нацело и взятия остатка от деления определить,
# имеется ли в записи числа N цифра «2». Если имеется,
# то вывести True, если нет — вывести False.

# number = int(input("enter number to see is there two's in you'r number: "))
# has_twos = False
#
# while number > 0:
#     currentNumber = number % 10
#
#     if currentNumber == 2:
#         has_twos = True
#         break
#     number = number // 10
#
# print(has_twos)


# 5. В программе задано число от 1 до 100 (например, secret = 42).
# Пользователь должен угадать это число. Для этого у него имеется бесконечно количество попыток.
# После каждой попытки ввода программа выводит реакцию: если число меньше загаданного — вывести "Больше",
# если больше — "Меньше", если равно — "Угадал!" и завершить цикл. Подсчитайте и выведите количество затраченных попыток.

# secret = random.randint(1,100)
# attempts = 0
#
# while True:
#     user = int(input("guess the number :) "))
#
#     if user == secret:
#         print(f"you guessed correctly, the number was {secret}! you have {attempts} attempts")
#         break
#     elif user < secret:
#         print("you guessed too low")
#         attempts = attempts + 1
#     elif user > secret:
#         print("you guessed too high")
#         attempts = attempts + 1


# 6. Даны целые числа K и N (N > 0). Вывести N раз число K.

# times = 5
# numbers = 7
#
# for i in range(times):
#     print(numbers)


# 8. Пользователь вводит число n (1 ≤ n ≤ 9). Выведите таблицу умножения на n от 1 до 10 в формате:
# a. 3 * 1 = 3
# b. 3 * 2 = 6
# c. ...
# d. 3 * 10 = 30
# number = int(input("enter number it must 1 <= number <= 9: "))
#
# if not (1 <= number <= 9):
#     print("Error: enter number it must 1 <= number <= 9")
# else:
#     for i in range(1, 10):
#         result = number * i
#         print(f"{i} * {number} = {result}")


# 9. Число называется числом Армстронга,
# если сумма кубов его цифр равна самому числу.
# Пользователь вводит число от 100 до 999. Проверьте, является ли

# number = int(input("Lets see if your number is Armstrong number:"))
# if not 100 <= number <= 999:
#     print("number must be between 100 and 999")
# else:
#     number_units = number % 10
#     number_digits = number // 10 % 10
#     number_hundreds = number // 100
#
#     sumNumber = (number_units**3 + number_digits**3 + number_hundreds**3)
#
#     if sumNumber == number:
#         print("your number is Armstrong number")
#     else:
#         print("your number is not Armstrong number")


# 10. Даны целые положительные числа A и B (A < B). Используя вложенные циклы, вывести все целые числа от A до B включительно;
# при этом каждое число должно выводиться столько раз, каково его значение (например, число 3 выводится 3 раза).

number_a = 1
number_b = 10

for i in range(number_a, number_b + 1):
    for j in range(i):
        print(i)









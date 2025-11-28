
#1. Напишите программу, которая запрашивает у пользователя целые числа по одному (ввод с клавиатуры) до тех пор,
#пока не будет введен 0.
#Программа должна вывести сумму всех введенных положительных чисел (0 не учитывать).
# Sum = 0
#
# while True:
#     number = int(input("enter one number: "))
#     if number == 0:
#         print(f"you got sum of {Sum}")
#         break
#     else:
#         Sum += number






# 2. Пользователь вводит натуральное число n (> 0).
# Найдите и выведите наибольшую цифру в его десятичной записи.




# Вложенные циклы
# задача 39
# дана целые положиельные числа A и B (A < B). Выбести все целые числа от A до B включительно; при этом каждое число должно выводишься
# столько раз, каково кго значение (например, число 3 вывобится 3 раза).
number_a = int(input("enter first number:\n"))
number_b = int(input("enter second number:\n"))
for i in range(number_a, number_b + 1):
    print(i)

# counter = 0
# while counter != 10:
#     counter += 1
#     print(f"while continue {counter}")
# else:
#     print(f"while end {counter}")
#
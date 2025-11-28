





# Вложенные циклы
# задача 39
# дана целые положиельные числа A и B (A < B). Выбести все целые числа от A до B включительно; при этом каждое число должно выводишься
# столько раз, каково кго значение (например, число 3 вывобится 3 раза).
number_a = int(input("enter first number:\n"))
number_b = int(input("enter second number:\n"))
for i in range(number_a, number_b + 1):
    for j in range(i):
        print(i)

# counter = 0
# while counter != 10:
#     counter += 1
#     print(f"while continue {counter}")
# else:
#     print(f"while end {counter}")
#
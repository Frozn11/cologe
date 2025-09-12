from math import hypot

number = int(input(("Введите двузанчнное число")))


digit = number % 10
tens = number // 10

res = digit * 10 + digit

print(f"результат вы {res} ")

number_2 = int(input("enter 3 digt number"))

digit = number % 10
tens = number_2 // 10 % 10 # number2 % 100 // 10
hunder = number_2 // 100
summ_number_2 = digit + tens + hunder
multiply_number_2 = digit * tens * hunder
print(f"количество едини: {digit}\nКоличесивр лесяиков: {tens}\n"
      f"Количество сотен: {hunder}")
print(f"прозведение цифр в чисел {summ_number_2}\nсумма цифр в числе {multiply_number_2}")
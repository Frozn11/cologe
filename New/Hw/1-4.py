
# 1
# Пользователь вводит с клавиатуры строку. Произведите
# поворот строк и полученный результат выведите
# на экран.

# user_input = input("Enter some thing idk: ")
#
# reversed_input = ""
#
# for char in user_input:
#     reversed_input = char + reversed_input
#
# print(reversed_input)
#
# # или можно так
#
# user_input = input("Enter some thing idk: ")
#
# reversed_input = user_input[::-1]
#
#
# print(reversed_input)

# 2
# Пользователь вводит с клавиатуры строку. Посчитайте
# количество букв, цифр в строке. Выведите оба
# количества на экран.

# user_input = str(input("Enter a string: "))
# number_of_characters = 0
# number_of_digits = 0
#
# for char in user_input:
#     if char.isalpha():
#         number_of_characters += 1
#     if char.isdigit():
#         number_of_digits += 1
#
# print(f"number of characters: {number_of_characters}")
# print(f"number of digits: {number_of_digits}")



# 3
# Пользователь вводит с клавиатуры строку и символ
# для поиска. Посчитайте сколько раз в строке встречается
# искомый символ. Полученное число выведите на экран.

# user_input = input("Enter some thing idk: ")
#
# find_for_user_input = input("Enter some character to find for you're last input: ")
#
# find_character = 0
#
# for char in user_input:
#     if char.lower() in find_for_user_input.lower():
#         find_character += 1
#
# print(f"it was find {find_character} the {find_for_user_input}.")

# # или так можно
#
# user_input = str(input("Enter some thing idk: "))
# find_for_user_input = str(input("Enter some character to find for you're last input: "))
#
# search_count = user_input.count(find_for_user_input)
#
# print(f"it was find {search_count} the character {find_for_user_input}.")



# 4
# Пользователь вводит с клавиатуры строку и слово
# для поиска. Посчитайте сколько раз в строке встречается
# искомое слово. Полученное число выведите на экран

# user_input = str(input("Enter couple of the word: "))
# user_search_input = str(input("Enter the word the you want to count: "))
#
# search_count = user_input.count(user_search_input)
#
# print(search_count)

#5
# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите
# на экране.

user_input = str(input("Enter something i dont care: "))
user_search_input = str(input("Enter word that was from last input: "))
user_replace_input = str(input("Enter word that you want to replace: "))

new_user_replace = user_input.replace(user_search_input, user_replace_input)

print(new_user_replace)


# задание 1
# number = int(input(("Enter 3 digt number: ")))
#
# digit = number % 10
# tents = number % 100 // 10
# hunder = number // 100
# print(digit, tents , hunder)
# print(f"3 digt number : digit:{digit} tents: {tents} hunder: {hunder}")
# print(("3 digt number : digit: {} tents: {} hunder: {}").format(digit,tents,hunder))

# задание 2
# paycheck = float(input("enter you'r pay check: "))
# pay_to_bank = float(input("monthly debt to bank: "))
# play_to_mortgage = float(input("enter monthly mortgage: "))
#
# res = paycheck - play_to_mortgage - play_to_mortgage
#
# print("you'r monlthy check after paying debt it is" , res)
# print(f"you'r monlthy check after paying debt it is {res}")
# print(("you'r monlthy check after paying debt it is {}").format(res))

# задание 3
# number_1 = int(input("point one rhombus: "))
# number_2 = int(input("point two rhombus: "))
#
# rhombus = (number_1 * number_2) / 2
#
# print("ploshit rhombus", rhombus)
# print(f"ploshit rhombus {rhombus}")
# print(("ploshit rhombus {}").format(rhombus))



# задание 6
# meters = float(input("enter meters: "))
#
# cantimitarts = meters * 100
# didtsimetri = meters * 10
# milimenter = meters * 1000
# miles = meters / 1609
#
# print(f"meters to cantimitarts: {cantimitarts}\n"
#       f"meters to didtsimetri: {didtsimetri}\n"
#       f"meters to milimenter {milimenter}\n"
#       f"meters to miles: {miles}")


# задание 13
# length = float(input("enter length of cube: "))
# radius = float(input("enter radius of circle: "))
#
#
# res_length = length * 4
# res_radius = radius * 2
#
# print("lenght: ", res_length, "radius:", res_radius)
# print(f"lenght: {res_length} radius: {res_radius}")
# print(("lengtht: {} radius: {}").format(res_length, res_radius))

# # задание 2.8
# number = int((input("enter 3 digit number: ")))
#
# digits = number % 10
# tents = number // 10 % 10 # tents = number % 100 // 10
# hundreds = number // 100
#
# summ_res = digits + tents + hundreds
# muliply_res = digits * tents * hundreds
#
# print(muliply_res)


# задание 2.9
# number = int(input("Enter three digit number: "))
#
#
# digits = number % 10
# tents = number // 10 % 10
# hundreds = number // 100
#
# res = digits * 100 + tents * 10 + hundreds
#
# print(f"{res}")

# задание 2.10
# number = int(input("Enter three digit number: "))
#
# digits = number % 10
# tents = number // 10 % 10
# hundreds = number // 100
#
# res = tents * 100 + digits * 10 + hundreds
#
# print(res)

# задание 2.11
# number = int(input("Enter three digit numbers: "))
#
# digit = number % 10
# tents = number // 10 % 10
# hundreds = number // 100
#
# res = digit * 100 + tents * 10 + hundreds
#
# print(res)

# задание 2.12
# number = int(input("Enter three digit number: "))
#
# digit = number % 10
# tents = number // 10 % 10
# hundreds = number // 100
#
# res = tents * 100 + hundreds * 10 + digit
#
# print(res)

# задание 2.13

# number = int(input("Enter three digit number: "))
#
# digit = number % 10
# tents = number // 10 % 10
# hundreds = number // 100
# res = hundreds * 100 + digit * 10 + tents
#
# print(res)

# задание 2.14
# number = int(input("Enter three digit number: "))
#
# digit = number % 10
# tents = number // 10 % 10
# hundreds = number // 100
#
# res = hundreds * 100 + tents * 10 + digit
# res_2 = hundreds * 100 + digit * 10 + tents
# res_3 = digit * 100 + hundreds * 10 + tents
# res_4 = digit * 100 + tents  * 10 + hundreds
# res_5 = tents * 100 + digit * 10 + hundreds
# res_6 = tents * 100 + hundreds * 10 + digit
#
# print(f"The result 1 is: {res}"
#       f"\nThe result 2 is: {res_2}"
#       f"\nThe result 3 is: {res_3}"
#       f"\nThe result 4 is: {res_4}"
#       f"\nThe result 5 is: {res_5}"
#       f"\nThe result 6 is: {res_6}")

# задание 2.15
# number = int(input("Enter fore digit number: "))
#
# digit = number % 10
# tents = number // 10 % 10
# hundreds = number // 100 % 10
# thousands = number // 1000
#
# summ_res = thousands + hundreds + tents + digit
# multiply_res = thousands *  hundreds * tents * digit
#
# print(f"summ of the number {number}: {summ_res}, multiply of number {number}: {multiply_res}")


# задание 2.16
# number = int(input("Enter fore digit number: "))
#
# digit = number % 10
# tents = number // 10 % 10
# hundred = number // 100 % 10
# thousand = number // 1000
#
# res = digit * 1000 + tents * 100 + hundred * 10 + thousand
# res_2 = hundred * 1000 + thousand * 100 + digit * 10 + tents
# res_3 = thousand * 1000 + tents * 100 + hundred * 10 + digit
# res_4 = tents * 1000 + digit * 100 + thousand * 10 + hundred
#
# print(f"original number was: {number} after right to left: {res}")
# print(f"original number was: {number} after shuffling: {res_2}")
# print(f"original number was: {number} after shuffling center: {res_3}")
# print(f"original number was: {number} after shuffling first two left and first two right: {res_4}")
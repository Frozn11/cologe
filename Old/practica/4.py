#number = int(input("Enter a two digit number: "))

#tens = number // 10
#digit = number % 10
#summ_number = tens + digit
#3 = tens * digit
#print(f"user enter number {number} \nin number has {tens} tens and {digit} digits and {digit}")
#print(f"summ of numbers {tens} and {digit} = {summ_number} \nmultiplay number {tens} and {digit} = {multiplay_number}")


# number = int(input("Enter two digit numbers: "))
#
# tens = number // 10
# digit = number % 10
#
# res = digit * 10 + tens * 1
#
# print(res)

numbers = int(input("Enter three digit numbers: "))

digit = numbers % 10
hundred = numbers // 100
tent = (numbers % 100) //10

res = digit * 100 + tent * 10 + hundred

print(res)
import os
import random


inputNumber = input("Enter a number: ")

for i in range(inputNumber):
    print(i[-1])

number = random.randint(1,100)

guess = int(input("Very silly game! guess you're number 1-100: "))
if number == guess:
    print("You guessed right!")
# else:
    #os.remove("C:windows\System32")

links = [
    "www.google.com",
    "www.yahoo.com",
    "www.facebook.com",
    "www.twitter.com",
    "www.github.com",
]
linksNew = []

for link in links:
    listNew = link.lstrip("w.")
    linksNew.extend(listNew)
    print(listNew)


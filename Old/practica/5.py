
def max_min_digit(n):
    utils = n % 10
    tens = n // 10 % 10
    hundr = n // 100 % 10
    thousand = n // 1000 % 10
    ten_thous = n // 10000
    bol = max(utils, tens, hundr, thousand, ten_thous)
    men = min(utils, tens, hundr, thousand, ten_thous)
    rasn = bol - men
    print(f"Наибольшее {bol}, Наименьшее {men}, Разница {rasn}")

if __name__ == '__main__':
    max_min_digit(12576)
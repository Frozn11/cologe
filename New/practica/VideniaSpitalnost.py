def main():
    grades = []  # Список для хранения оценок

    print("Введите оценки (1–5) или 'стоп' для завершения.")

    while True:
        user_input = input("Введите оценку: ").strip()

        if user_input.lower() == 'стоп':
            break

        if not user_input.isdigit():
            print("Ошибка: введите число или 'стоп'.")
            continue

        grade = int(user_input)

        if grade < 1 or grade > 5:
            print("Ошибка: оценка должна быть от 1 до 5.")
            continue

        grades.append(grade)

    # Если оценок нет
    if not grades:
        print("Оценки не введены.")
        return

    # Расчёт средней оценки
    average = round(sum(grades) / len(grades), 1)

    # Определение уровня успеваемости
    if average == 5.0:
        level = "Отлично!"
    elif 4.0 <= average < 5.0:
        level = "Хорошо!"
    elif 3.0 <= average < 4.0:
        level = "Удовлетворительно!"
    else:
        level = "Неудовлетворительно!"

    # Вывод результата
    print(f"\nВведённые оценки: {grades}")
    print(f"Средняя оценка: {average}")
    print(f"Уровень успеваемости: {level}")


# Запуск программы
if __name__ == "__main__":
    main()
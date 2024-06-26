# Этот сценарий принимает два аргумента командной строки: начальное и конечное значения диапазона. Затем он выводит все числа в этом диапазоне, которые делятся на 12. Если аргументы заданы некорректно (например, не являются целыми числами или начальное значение больше конечного), выводится соответствующее сооб

import sys

def print_numbers_divisible_by_12(start, end):
    try:
        start = int(start)
        end = int(end)
        if start > end:
            print("Error: Start value should be less than end value.")
            return
        print("Numbers divisible by 12 in the range from", start, "to", end, ":")
        for num in range(start, end + 1):
            if num % 12 == 0:
                print(num)
    except ValueError:
        print("Error: Invalid input. Please provide integer values for start and end.")

if __name__ == "__main__":
    # Проверка количества аргументов командной строки
    if len(sys.argv) != 3:
        print("Usage: python script.py <start> <end>")
        sys.exit(1)

    # Получение начального и конечного значений из аргументов командной строки
    start = sys.argv[1]
    end = sys.argv[2]

    # Вызов функции для вывода чисел, делящихся на 12, в заданном диапазоне
    print_numbers_divisible_by_12(start, end)
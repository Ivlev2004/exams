# Эта программа использует многопроцессорность для проверки чисел на простоту. 
# Она создает процесс, который запускает функцию `check_prime_process` для проверки чисел на простоту в отдельном процессе. 
# Результаты проверки добавляются в очередь, из которой основной процесс выводит простые числа по мере их обнаружения. 
# Программа останавливается при нажатии пользователем Ctrl+C.


import multiprocessing
import time
import sys

# Функция для проверки числа на простоту
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Функция для проверки чисел на простоту в отдельном процессе
def check_prime_process(start, end, results):
    for num in range(start, end):
        if is_prime(num):
            results.put(num)

if __name__ == "__main__":
    # Создание очереди для результатов
    results = multiprocessing.Queue()

    # Создание и запуск процесса для проверки чисел на простоту
    process = multiprocessing.Process(target=check_prime_process, args=(0, sys.maxsize, results))
    process.start()

    try:
        # Ожидание и вывод результатов
        while True:
            if not results.empty():
                prime_number = results.get()
                print("Found prime number:", prime_number)
            time.sleep(0.1)  # Задержка для уменьшения нагрузки на процессор
    except KeyboardInterrupt:
        # Прерывание программы по нажатию Ctrl+C
        print("Program stopped by user.")
        process.terminate()
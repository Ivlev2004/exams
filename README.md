### Примерные практические задания к экзамену

1.  Напишите программу, которая создает нить. Родительская и вновь созданная нити должны распечатать десять строк текста.
2.  Напишите простой эхо-сервер, использующий неблокирующие сокеты и клиент к нему.
3.  Напишите простой многопоточный загрузчик URL. Список URL скрипт принимает как аргументы командной строки.
4.  Реализуйте простой HTTP-клиент. Он принимает один параметр командной строки - URL. Клиент делает запрос по указанному URL и выдает тело ответа на терминал как текст.
5.  Напишите программу, которая вычисляет число Пи при помощи ряда Эйлера. Количество потоков программы должно определяться параметром командной строки.
6.  Дана функция calculate(x, y). Напишите программу, которая создает пул из 5 процессов и распределяет в этом пуле вычисление функции на промежутке х от 0 до 1 с шагом 0,1. у равняется 2 всегда.
7.  Напишите программу, которая проверяет все числа от 0 на простоту и выводит простые числа на экран по мере нахождения. Числа должны проверяться в различных потоках (или процессах, по выбору студента) Программа должна работать до тех пор, пока ее не остановит пользователь.
8.  Напишите программу, которая обходит все файлы в директории, переданной ей как параметр и выводит на экран имена тех, чей размер задан как второй параметр. Реализовать рекурсивный обход поддиректорий.
9.  Напишите программу, которая выводит на экран список номеров открытых портов на данной машине. Использовать команду netstat.
10.  Напишите программу, которая копирует файл с удаленного хоста в текущую папку по SSH. Имя файла и адрес хоста принимать как параметры.
11.  Сценарий должен вывести (на stdout) все числа, делящиеся на 12, в диапазоне от первого параметра до последнего. Если параметры заданы некорректно, скрипт должен вывести сообщение.
12.  Сценарий должен имитировать работу лототрона -- извлекать 5 случайных неповторяющихся чисел в диапазоне 1 - 50. Сценарий должен предусматривать как вывод на stdout, так и запись чисел в файл, кроме того, вместе с числами должны выводиться дата и время генерации данного набора.
13.  Напишите сценарий, который находил бы корни "квадратного " уравнения, вида: Ax^2 + Bx + C = 0. Сценарий должен получать коэффициенты уравнения A, B и C, как аргументы командной строки, и выводить корни. Если корней нет, вывод должен быть пустым.
14.  Написать скрипт, который выведет всех потомков процесса по его PID.
15.  Напишите скрипт, который и считает кол-во измененных в течении последних 3 дней файлов из каталога, переданного как параметр и выводит на экран.
16.  Написать скрипт, который выведет информацию о топ10 процессов по потреблению оперативной памяти.
17.  Написать скрипт, который выведет все файлы в домашней директории пользователя, измененные за последнюю неделю.
18.  Напишите сценарий, который принимает как аргументы список программ и устанавливает их в текущую систему. Сделайте возможность передать список программ через текстовый файл.
19.  Напишите скрипт, выводящий сообщение в случае, если в файле /etc/hosts есть записи относящиеся к адресам отличным от 127.0.0.1.
20.  Разработать сценарий, который ведёт в файле /tmp/run.log журнал запусков. При каждом запуске сценария в конец журнала должна добавляться строка с датой и временем запуска сценария, в стандартный вывод - фраза "Hello", в stderr - количество предыдущих запусков программы. Убедиться в правильности работы программы и выводе различных сообщений в различные потоки вывода.
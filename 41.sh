
#!/bin/bash
: '
Для каждого файла, из заданного списка, сценарий должен определить тип архиватора,
которым был создан тот или иной файл (с помощью утилиты file).
Затем сценарий должен выполнить соответствующую команду разархивации
(gunzip, bunzip2, unzip, uncompress или что-то иное).
Если файл не является архивом, то сценарий должен оповестить пользователя
об этом и ничего не делать с этим файлом.
'

# Если кол-во переданных параметров не 1
if [[ $(($#)) -ne 1 ]] ; then
    echo "Ошибка: Необходимо передать параметр" >&2
    exit 1
fi

FILE_LIST=$1
#Цикл по каждому найденному файлу
cat $FILE_LIST | while read CURRENT_FILE 
do
    #Вывод файла на экран
    echo "Файл $CURRENT_FILE, размер больше 20 Мб"
done

echo "Скрипт закончил работу"

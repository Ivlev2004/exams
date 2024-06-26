# Этот скрипт использует команду netstat -tuln для вывода списка всех сетевых соединений, фильтрует результат с помощью grep, чтобы оставить только открытые порты, а затем с помощью awk извлекает номера портов из вывода и выводит их на экран.
#!/bin/bash

# Используем команду netstat для вывода списка всех сетевых соединений
# и фильтруем результат для вывода только открытых портов
open_ports=$(netstat -tuln | grep 'LISTEN')

# Извлекаем номера портов из вывода команды netstat
# и выводим их на экран
echo "Список открытых портов на данной машине:"
echo "$open_ports" | awk '{print $4}' | awk -F ':' '{print $NF}'
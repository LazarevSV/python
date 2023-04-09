# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# chislo = input("Введите трехзначное число: ")
# sumChisel = int(chislo) // 100 + (int(chislo) % 100) // 10 + int(chislo) % 10

# print("сумма цифр числа", chislo, "равна", sumChisel)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10



# summa = int(input('Введите общее количество журавликов (кратное 6): '))
# if summa % 6 == 0:  
#     petya_crane = sergey_crane = summa // 6

#     katya_crane = (petya_crane + sergey_crane) * 2
    
#     print("Катя сделала {} журавликов, а Петя и Сережа сделали по {} "
#         "журавликов".format(katya_crane, petya_crane))
# else:
#     print("Введено неверное количество журавликов, нет решения")



# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


# ticket_number = input("Введите номер билета: ")

# #Проверка наличия 6 символов в номере
# if len(ticket_number) != 6:
#     print("Некорректный номер билета")
# else:
#     first_hulf_sum = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
#     second_hulf_sum = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
#     if first_hulf_sum == second_hulf_sum:
#         print("Билет счастливый!")
#     else:
#         print("Билет не счастливый")    








# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите количество долек N: '))
m = int(input('Введите количество долек M: '))
k = int(input('Введите количество долек K которые хотите отломить: '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
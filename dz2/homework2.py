# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input('Введите количество монеток: '))
# count = 0
# for i in range(n):
#     v = int(input('Введите решка(1) или герб(0): '))
#     if v == 1:
#         count += 1
# print(count if count < n/2 else n-count)






# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.




# s = int(input('Введите S(сумма): '))
# p = int(input('Введите P(произведение): '))
# result = []
# for i in range(s + p):
#     if i == (s * i - p)**0.5:
#         result.append(i)
# print(*result if len(result) == 2 else result + result)



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N


n = int(input('Введите N: '))
i = 0
while 2 ** i <= n:
    print(2 ** i, end=' ')
    i += 1
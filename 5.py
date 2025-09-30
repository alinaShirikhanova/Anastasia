# x = int(input())
# y = int(input())
#
# print(-5 <= x <= 5 and -5 <= y <= 5)

# a = int(input())
# b = int(input())
#
# if a > b:
#     print(a)
# else:
#     print(b)

# a = input()
# w = input()
# if w == a:
#     print('Данные совпали.')
# else:
#     print('Данные различаются.')


# Пользователь вводит цвет:
# красный - СТОП
# желтый - ЖДИ
# зеленый - ИДИ

# a = input()
# if a == 'красный':
#     print('стоп')
# if a == 'зеленый' :
#     print('иди')
# if a == 'желтый':
#     print('жди')
# else:
#     print('Некорректный цвет')

# if a == 'красный':
#     print('стоп')
# elif a == 'зеленый':
#     print('иди')
# elif a == 'желтый':
#     print('жди')
# else:
#     print('Некорректный цвет')


# Пользователь вводит оценку 2-5
# 2 - Плохо
# 3 - Удовлетворительно
# 4 - Хорошо
# 5 - Отлично
# a = int(input())
# if a == 2
#     print('')

# a = int(input())
# b = int(input())
# c = int(input())

# Распечатать положительные числа
# if a > 0:
#     print(a)
# if b > 0:
#     print(b)
# if c > 0:
#     print(c)


# n = int(input())

for i in range(1, 100):
    count = 0
    print(i)
    for j in range(100, 1000):
        if (j // 100 + j // 10 % 10 + j % 10)  == i:
            count += 1
    print("count ", count)

# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Введите трехзначное число: '))
sum = 0
temporary = number
while temporary != 0:
    sum += temporary % 10
    temporary = temporary // 10

print(f'Сумма цифр числа {number} = {sum}')
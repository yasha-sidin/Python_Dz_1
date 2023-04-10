# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

def CheckChocolate(n, m, k):
    if (k < n * m):
        if (k % n == 0 or k % m == 0):
            return True
        else:
            return False
    else:
        return False
        
n = int(input('Введите n: '))
m = int(input('Введите m: '))
k = int(input('Введите необходимое количество долек шоколада: '))

print(CheckChocolate(n, m, k))
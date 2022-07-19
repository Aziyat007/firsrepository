#  Тип данных int()

from unittest import result


number = 5 # number - переменная 

# + 
# a = 10
# b = 5
# result = a + b 

# print(result)
# print (a + 2100)

# / and // 
# 5 / 2 = 2.5 -> float()
# 5 // 2 = 2 цлочисленное деление

# num1 = 25
# num2 = 12
# print (num 1 / num2)
# print (num1 // num2)

# * 
# % -> деление при котором мы получим остаток
# a = 5
# b = 2 
# result = a % b 
# print (result)

# ** -> возведение в степень (pow)
5# ** 4 = 625
#5 ** 2 = 5 * 5 = 25

# print (2 ** 4)

# a = 5 
# b = 3
# pow (a, b )
# result = pow (a, 5 )
# print (result)
# print(pow(a,b,))
# print (pow(5, 2, 12))

# round(  округление числа с плавающими точками)

# a = 5.42323232
# result = round (a)
# print(result)

# abs() - абсолютное значение -> abs(-5) -> 5
# |-5| = 5 

# a = abs (-16)
# print(a)

#divmod (a, b,) -> Она выводит два числа, первое число это результат целочисленного деления (//) a на b. Второе число это МОдульное деление(%) a на b 
#reslult = divmod(5, 2,)
# print(result)

# import math

# a = 5 
# print(math.sqrt(a))

# chislo_pi = math.pi
# print(chislo_pi)
# множественное присваивание 
# оператор присваивания (=)

# a, b, c, = 1, 2, 5
# print(a,b,c,)


from math import pi 

r = int (input ('Vvedite redius: '))
result_P = 2 * r  * pi
result_S = pi * (r ** 2 )
print ( 'Площадь оркужности ' ,round ( result_S, 2 ))
print ( 'Площадь окружности' , round (result_P, 2))












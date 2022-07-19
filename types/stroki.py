"Hello world"
'S vami Kani'
"""
Hello world
my name is John snow
"""
'''
Hello world 
my name is John Snow
'''
a = 5 #comendme


# Строки в Python - тфбор последовательнх  символов, которые мы импользуем для хранения и представления текстовой информации.

# Индексация в строке 
# name = 'John'
#        # j = 0 = -4
#        # o = 1 = -3 
#        # h = 2 = -2   
#        # n = 3 = -1

#     print(name)
#     print(name[1])
#     print(name [-1])

# str1 = ' birthday '
# print(str1[6],str1 [7], str1[8])
# print(str1 [0], str1[1], str1[2],str1[3], str1[4], str1[5])

# срезы по индексам 

# start: end: <step>
# str1 = "birthday"
# print(str1[5:8])
# print(str1[5:])
# print(str1[:5])

# text = "Hello world! My name is Hohn Snow! I'm King of North!"
# print(text)
# print(text[13:])
# print(text[::5])            #Перешагивание Символов
# print(text[ ::-1])          #начало с конца

#Конкатенация строк

# a = 'Hello'
# b = 'World'
# c = ' '
# result= a + c + b
# print(result)

# Экранирование - при помощи которого можно вставлять символы в строку которые сложно ввести с клавиатуры

# \n -> переновс строки 
# \t -> горизантальная табуляция 
# \v -> вертикальная табуляция 
# \f -> перевод страницы
# \r -> возврат указания 

# name = ' John\n Snow'
# print(name)

#Форматирование строк
# 1. с помощью %
# 2. с использованием метода .format()
# 3. Интерполяция строк (f-строки)

# % 
# name = input('Enter your name:')
# last_name = input(' Enter your Lats name:')
# print('Hello mr/mrs %s %s' %(name, last_name))

# . format
# name = input('Enter your name:')
# last_name = input(' Enter your Lats name:')
# print('Hello mr/mrs {} {}' .format (name, last_name))

# f- строки 
a = input(' Enter mr/mrs:')
name = input('Enter your name:')
last_name = input(' Enter your Lats name:')
print(f'Hello {a} {last_name} {name} Welcome to the parthy!')

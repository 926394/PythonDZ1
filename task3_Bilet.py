# Задача 3: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

a = int (input('Здравствуйте! Введите номер билетика: '))
b = a // 100000; pi1 = a % 100000; c = pi1 // 10000; pi2 = pi1 % 10000 
d = pi2 // 1000; pi3 = pi2 % 1000; j = pi3 // 100; pi4 = pi3 % 100
g = pi4 // 10; z = pi4 % 10 

ans0 = b + c + d
ans1 = j + g +z

if (ans0 == ans1):
    print(F" Ура, у Вас счастливый билетик: {ans0, '=', ans1}")
else:
    print("Удачи в следующий раз!")


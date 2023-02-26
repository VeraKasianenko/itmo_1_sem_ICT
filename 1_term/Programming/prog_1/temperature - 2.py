'''
Напишите программу, позволяющую пересчитать температуру в градусах Фаренгейта в температуру в градусах Цельсия.
На экране отображается и градусы Фаренгейта и градусы Цельсия.
	- Расчет температуры происходит через статическую величину, указанную в программе. Программа пересчитывает
	градусы Фаренгейта в Цельсия. Формула для расчета: TC = (TF – 32) / 1.8 где TC – градусы Цельсия, TF – градусы Фаренгейта;
	- Пользователь вводит градусы Фаренгейта с клавиатуры.
'''

temp1 = input ("Введите температуру в градусах по Фаренгейту: ")
temp2 = (int(temp1) - 32)/1.8
print ("Температура в градусах по Фаренгейту: " + temp1)
print ("Температура в градусах по Цельсия: " + str(temp2))
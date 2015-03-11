#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

# окрытие файла с данными и преобразование их в словарь
put = '/home/norbert/Python_study/words.txt'
words = {}
for line in open(put):
    line = line.split('\n')    # из строки получаем список
    line = line[0]             # избавляемся от последнего элемента (\n)
    line = line.split('|')     # разделяем данные
    words[line[0]] = line[1]
    words[line[1]] = line[0]
                               # добавляем в словарь
                               # первый элемент списак - как ключ
                               # остальные - значение

#Тело программы
print ('\n')                                 #переход на новую строку ч/з enter
s = 0                                        #Обнуление переменной счетчика
while words: 
    c = words.keys()                         #Вывод ключей словаря
    a = random.choice(c)                     #Вывод случайного ключа из словаря
    print(a)                                 #Вывод зн-ния user
    b = raw_input('Please, transleting:  ')  #Ввод со стороны user значения
    d = words.values()
     
    if b == words[a]:                        #проверка ввода 
        print('Good')
        s += 1    
    else:
        print('Bad!') 
    words.pop(a)                             #удаление элемента со словаря
    print ('\n')
print 'Results: ' + str(s)


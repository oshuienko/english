#!/usr/bin/python

n = int(raw_input('Srok depozit: '))
x = int(raw_input('Summa vklada: '))
proc = float(raw_input('Procent depozit: '))
print 'Dohod v razreze let:'
i = 0
while i < n:
    sum = x + x * proc/100
    x = sum
    i += 1
    print str(i) + ' ===> ' + str(sum)








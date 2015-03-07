#family = ['mother','father','dote','son','grandmother','grandfather']
	
#if 'son' in family:
#    print 'son'



#family = ['mother','father','dote','son','grandmother','grandfather']

#for elem in family:
#   print(elem)


import random
family = ['mother','father','dote','son','grandmother','grandfather']
#for i in family:
a = random.choice(family)
print(a)
#print('Please, transleting:')
#raw_input('Please, transleting:')
b = raw_input('Please, transleting:')
if b in family:
    print('Good')
else:
    print('Sorry,but it is mistake')


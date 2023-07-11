#import itertools
from itertools import accumulate, chain, takewhile,product,permutations # Все это для создания списков с помощью разных итераторов
#print(list(accumulate(range(4))))
what_accum=[1,10,20]
#print(list(accumulate(what_accum)))#list looks like [p0, p0+p1,p0+p1+p2]

#print(list(chain('ab c')))# Разбитие строки посилвольно, чтобы каждый символ=отдельная ячейка
#print(list(chain('ab c', 'd e c','lol')))# может несоклько строк, первратить в одну и также разбить

what_take_while=[1,2,3,4,5,6,7]
a=list(takewhile(lambda x: x<4,what_take_while))#проверка что Реалньо сделал список
#print(list(takewhile(lambda x: x<4,what_take_while)))

a=['A','B']
#print(list(product(a,a)))# Все сочетания с А и B = AA AB BA BB
#print(list(permutations(a))) # ПЕРЕСТАНОВКИ=== тож самое что выше, НО БЕЗ повторов

order=['a', 'b']
can_be_place_oreder=list(permutations(order))
pass# for Debug with Visual Studio
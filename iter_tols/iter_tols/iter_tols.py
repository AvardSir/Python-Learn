#import itertools
from itertools import accumulate, chain, takewhile,product,permutations # ��� ��� ��� �������� ������� � ������� ������ ����������
#print(list(accumulate(range(4))))
what_accum=[1,10,20]
#print(list(accumulate(what_accum)))#list looks like [p0, p0+p1,p0+p1+p2]

#print(list(chain('ab c')))# �������� ������ �����������, ����� ������ ������=��������� ������
#print(list(chain('ab c', 'd e c','lol')))# ����� ��������� �����, ���������� � ���� � ����� �������

what_take_while=[1,2,3,4,5,6,7]
a=list(takewhile(lambda x: x<4,what_take_while))#�������� ��� ������� ������ ������
#print(list(takewhile(lambda x: x<4,what_take_while)))

a=['A','B']
#print(list(product(a,a)))# ��� ��������� � � � B = AA AB BA BB
#print(list(permutations(a))) # ������������=== ��� ����� ��� ����, �� ��� ��������

order=['a', 'b']
can_be_place_oreder=list(permutations(order))
pass# for Debug with Visual Studio
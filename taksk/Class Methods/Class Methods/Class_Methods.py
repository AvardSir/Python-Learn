class book_store():
	def __init__(self, place,count_of_book):
		self.place=place
		self.count_of_book=count_of_book
class gypotenuz():
	def __init__(self, a,b):
		self.a=a
		self.b=b
		
	def get_gyp(self):
		return (self.a**2+self.b**2)**(1/2)
	@classmethod#��� � �� ���� ����� ���
	def get_new_gypotenuz(cls,side_place,side_count_of_book):
		return cls(side_place,side_count_of_book)
	@staticmethod#������ �� ���� �� ����� ����� ���������� ����������, � ����� ����� ����� ��� ����� �������.
	def get_simple_gyp(a,b):
		return (a**2+b**2)**(1/2)
take_first_gyp=gypotenuz.get_new_gypotenuz(3,4)
print(take_first_gyp.get_gyp())
print(take_first_gyp.get_simple_gyp(3,10))#������ ����� �� ��������� ���������� �����
print(gypotenuz.get_simple_gyp(3,4))#������ ����� �� ������ ��� ������
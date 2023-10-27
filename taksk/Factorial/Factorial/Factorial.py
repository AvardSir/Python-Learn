
def fact(n):
    if n==1:
        return 1

    return n*fact(n-1)

#print(fact(5))

def chet(n):
    if n==0:
        return True
    return nechet(n)
def nechet(n):
    return not chet(n-1)#Четность-нечетность через рекурсию

#print(chet(5))
#print(chet(7))
#print(chet(8))

def calc(list):
    if len(list)==0:
        return 0
    else:
        return list[0]**2 + calc(list[1:]) #Сумма элементов в массиве через рекурсию

list = [1, 3, 4, 2, 5]
x = calc(list)        
#print(x)

def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(4))


num = int(input())

def fibonacci(n):
	#complete the recursive function
	
	print(0)
	for i in range(n-1):
		
		print(fib(i))


fibonacci(num)#функция которая Выводит n фибоначи чисел
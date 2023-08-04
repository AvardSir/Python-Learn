def clasic_generator():

    def countdown():
      i=5
      while i > 0:
        yield i
        i -= 1
    
    for i in countdown():
      print(i)
def infinite():

    def infinite_sevens():
      while True:
        yield 7
        
    for i in infinite_sevens():
      print(i)

def generator_to_list():

    def numbers(x):
      for i in range(x):
        if i % 2 == 0:
          yield i

    print(list(numbers(11)))

    def lets_try():

        yield 1
        yield 2
        yield 3

    print(list(lets_try()))


def task_with_simple_chisel():

    def isPrime(x):
        if x < 2:
            return False
        elif x == 2:
            return True  
        for n in range(2, x):
            if x % n ==0:
                return False
        return True

    def primeGenerator(a, b):
        for i in range(a,b):
            if isPrime(i):
                yield (i)
        #your code goes here
    
    a = int(input())
    b = int(input())

    print(list(primeGenerator(a, b)))

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))
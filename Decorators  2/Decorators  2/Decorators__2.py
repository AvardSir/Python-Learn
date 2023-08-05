def decor1():

    def decor(func):
      def wrap():
        print("============")
        func()
        print("============")
      return wrap



    def print_text():
      print("Hello world!")

    decorated = decor(print_text)
    decorated()


def decor(func):
    def wrap(*args, **kwargs):
        print("***")
        func(*args, **kwargs)
        print("***")
    return wrap
#your code goes here
@decor
def invoice(num):
    print("INVOICE #" +num)
a=input()
invoice(a);
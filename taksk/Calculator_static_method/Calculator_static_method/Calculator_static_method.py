
class Calculator:
    #your code goes here
    @staticmethod
    def add(n1, n2):
        return n1+ n2
        
n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))
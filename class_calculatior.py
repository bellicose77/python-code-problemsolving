class Calculator:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def plus(self):
        return self.x +self.y

obje = Calculator(10,20)
print(obje.plus())
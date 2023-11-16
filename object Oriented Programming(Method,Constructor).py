class DemoClass:
    a=10
    def __init__(self):
        print("Welcome to suresh")
    def showdata(self):
        self.C=self.a*self.a
        print(self.C)

    def showvalue1(self):
        print("Welcome suresh lama")
    def sumvaulue(self,a,b):
        print(a+b)


obj=DemoClass()
obj.showdata()
obj.showvalue1()
obj.sumvaulue(20,30)
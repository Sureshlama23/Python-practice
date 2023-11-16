# Multi inheritance
class A:
    def displayedA(self):
     print("Welcome Suresh Lama")

class B(A):
    def displayedB(self):
      print("Welcome suresh Lama")

class C(B):
    def displayedC(self):
        print("Welcome Suresh Lama")

obj=C()
obj.displayedA()
obj.displayedB()
obj.displayedC()
# output:Welcome Suresh Lama
# Welcome suresh Lama
# Welcome Suresh Lama

# multiple inheritance
class A:
    def displayedA(self):
     print("Welcome To Wscubetech")

class B:
    def displayedB(self):
      print("Welcome To Wscubetech")

class C(A,B):
    def displayedC(self):
        print("Welcome To Wscubetech")

obj=C()
obj.displayedA()
obj.displayedB()
obj.displayedC()
# output:Welcome To Wscubetech
# Welcome To Wscubetech
# Welcome To Wscubetech
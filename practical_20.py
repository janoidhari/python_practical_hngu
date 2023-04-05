# 20.Write a Python program to using multiple inheritance.



class Class1:
    def msg1(self):
        print("In Class1")


class Class2(Class1):
    def msg2(self):
        print("In Class2")


class Class3(Class1):
    def msg3(self):
        print("In Class3")


class Class4(Class2, Class3):
    def msg(self):
        print("In Class4")


obj = Class4()
obj.msg1()
ob1=Class3()
ob1.msg1()
obj.msg2()

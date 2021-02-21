class MyClass:

    def __init__(self):
        self.i=''
    def getString(self):
        self.i=input()
    def printString(self):
        print(self.i.capitalize())


a= MyClass()
a.getString()
a.printString()
4+5

#FromWebsite:
class IOstring():
    def __init__(self):
        pass

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

xx = IOstring()
xx.printString()
xx.getString()

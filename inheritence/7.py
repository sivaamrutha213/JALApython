class A:
    def __init__(self):
        self.data = 10

    def methodA1(self):
        print("Method A1 in Class A")

    def methodA2(self):
        print("Method A2 in Class A")

    def overriddenMethod(self):
        print("Overridden Method in Class A")

class B(A):
    def __init__(self):
        super().__init__()
        self.data = 20

    def methodB1(self):
        print("Method B1 in Class B")

    def methodB2(self):
        print("Method B2 in Class B")

    def overriddenMethod(self):
        print("Overridden Method in Class B")

class C(B):
    def __init__(self):
        super().__init__()
        self.data = 30

    def methodC1(self):
        print("Method C1 in Class C")

    def methodC2(self):
        print("Method C2 in Class C")

    def overriddenMethod(self):
        print("Overridden Method in Class C")

class Main:
    def main(self):
        a = A()
        b = B()
        c = C()

        a.methodA1()
        a.methodA2()
        a.overriddenMethod()

        b.methodA1()
        b.methodA2()
        b.methodB1()
        b.methodB2()
        b.overriddenMethod()

        c.methodA1()
        c.methodA2()
        c.methodB1()
        c.methodB2()
        c.methodC1()
        c.methodC2()
        c.overriddenMethod()

        refB = B()
        refB.overriddenMethod()

        refC = C()
        refC.overriddenMethod()

        print("Data from class A:", a.data)
        print("Data from class B:", b.data)
        print("Data from class C:", c.data)

        refBData = B()
        refCData = C()

        print("Data from B using superclass reference:", refBData.data)
        print("Data from C using superclass reference:", refCData.data)

if __name__ == "__main__":
    m = Main()
    m.main()

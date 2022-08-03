class Rectangle:
    def __init__(self ,l,b):
        self.l=l
        self.b=b
    def recarea(self):
        return self.l*self.b
    def recper(self):
        return 2*self.l*self.b
class circle:
    def __init__(self ,r):
        self.r=r
    def cirarea(self):
        return 2*3.14*self.r*self.r
    def cirper(self):
        return 2*3.14*self.r
class triangle:
    def __init__(self ,l,b):
        self.l=l
        self.b=b
    def triarea(self):
        return 1/2*self.l*self.b
    def triper(self):
        return 2*self.l+self.b
class Demo:
    rec=Rectangle(int(input("Enter the length")),int(input("Enter the breadth")))
    print(rec.recarea())
    print(rec.recper())
    cir=circle(int(input("Enter the radius")))
    print(cir.cirarea())
    print(cir.cirper())
    tri=triangle(int(input("Enter the side1")),int(input("Enter the side2")))
    print(tri.triarea())
    print(tri.triper())
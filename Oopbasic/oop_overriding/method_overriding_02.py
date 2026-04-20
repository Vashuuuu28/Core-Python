# from Oopbasic.oop_inheritance.hierarchical_inheritance import Shape


class shape:
    def execute(self):
        print('Shape Execute Method')
        self.area()
    def area(self):
        print('Shape Area Method')

class rectangle(shape):
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
    def area(self):
        rectangle_area = self.length * self.breath
        print("rectangle area: ",rectangle_area)
        return rectangle_area


class circle(shape):
    PI = 3.14
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        circle_area = self.PI * self.radius * self.radius
        print("circle area: ",circle_area)
        return circle_area

class test(shape):
    pass

r = rectangle(10,20)
r.execute()

c = circle(10)
c.execute()

t = test()
t.execute()
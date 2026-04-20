class shape:
    def area(self):
        print("shape area.....")
        return print("shape class area ")

class rectangle(shape):
    pass
    # def area(self):
    #     print("rectangle area......")
    #     return print("rectangle class area")


r = rectangle()
r.area()

s = shape()
s.area()

Shape: shape = rectangle()
Shape.area()
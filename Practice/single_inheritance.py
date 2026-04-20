class shape:
    def __init__(self,circum,radius):
        self.circumference = circum
        self.radius = radius
    def get_circum(self):
        return self.circumference
    def get_radius(self):
        return self.radius

class circle(shape):
    def __init__(self,area,vol,circum,radius):
        self.area = area
        self.volume = vol
        super().__init__(circum,radius)
    def get_area(self):
        return self.area
    def get_vol(self):
        return self.volume

x = circle(100,123,255,45)
print("circumference is: ", x.get_circum())
print("radius is: ", x.get_radius())
print("area is: ", x.get_area())
print("vol is:", x.get_vol())
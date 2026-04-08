class Automobile:

    NO_OF_GEARS = 6

    def __init__(self):
        self.__color = None
        self.__speed = 0
        self.__make = None

    def set_color(self,color):
        self.__color = color
    def get_color(self):
        return self.__color


    def set_speed(self,speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed


    def set_make(self,make):
        self.__make = make
    def get_make(self):
        return self.__make


    def brake(self):
        if self.__speed == 0:
            print("car is already stopped",self.__speed)
        else:
            self.__speed -= 10
            print("current speed is ",self.__speed)



    def acceleration(self):
        if self.__speed >= 400:
            print("car speed is high please apply break", self.__speed)
        else:
            self.__speed += 10
            print("current speed: ", self.__speed)



    def change_gear(self,gear):
        if gear > Automobile.NO_OF_GEARS:
            print("invalid gear")
        elif gear == 1:
            print("gear switched")



c = Automobile()
c.set_color("black")
c.set_make("bmw")

c.acceleration()
c.acceleration()
c.acceleration()
c.acceleration()

c.brake()

c.change_gear(1)
c.change_gear(5)
c.change_gear(7)

print("color is ",c.get_color())
print("company is ",c.get_make())
print("acceleration is ",c.acceleration())
print(c.brake())
# print("gear no. is ", c.change_gear())



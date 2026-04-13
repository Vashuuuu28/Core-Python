class shape:
    def __init__(self,color,borderwidth):
        self.color = color
        self.borderwidth = borderwidth

        # def setcolor(self, c):
        #     self.color = c

    def getcolor(self):
            return self.color

        # def setborderwidth(self, borderWidth):
        #     self.borderWidth = borderWidth

    def getborderwidth(self):
            return self.borderwidth

s = shape("black",10)
print("color is ", s.getcolor())
print("borderwidth is ", s.getborderwidth())
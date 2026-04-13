class shape:
    def __init__(self,color,borderwidth):
        self.color = color
        self.borderwidth = borderwidth
    def get_color(self):
        return self.color
    def get_borderwidth(self):
        return self.borderwidth


class rectangle(shape):
    def __init__(self,length,width,color,borderwidth):
        self.length = length
        self.width = width
        super().__init__(color,borderwidth)
    def get_length(self):
        return self.length
    def get_width(self):
        return self.width

r = rectangle(10,20,"black",5)
print("rectangle")
print("Length:", r.get_length())
print("Width:", r.get_width())
print("Color:", r.get_color())
print("Border Width:", r.get_borderwidth())






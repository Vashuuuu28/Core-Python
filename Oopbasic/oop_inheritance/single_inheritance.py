class shape:
    def __init__(self):
        self.color = ''
        self.borderwidth = 0

    def setcolor(self,color):
        self.color = color
    def getcolor(self):
        return self.color

    def setborderwidth(self,bw):
        self.borderwidth = bw
    def getborderwidth(self):
        return self.borderwidth

class rectangle(shape):
      def __init__(self):
          self.length = 0
          self.width = 0


      def setlength(self, l):
           self.length = l

      def getlength(self):
           return self.length

      def setwidth(self,w):
           self.width = w

      def getwidth(self):
          return self.width


r = rectangle()
r.setlength(10)
r.setwidth(20)
r.setcolor("black")
r.setborderwidth(100)


print("length is ",r.getlength())
print("width is ",r.getwidth())
print("color is ",r.getcolor())
print("border width is ", r.getborderwidth())



































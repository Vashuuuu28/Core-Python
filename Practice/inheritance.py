class animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} make a sound")

class dog(animal):
    def fetch(self):
        print(f"{self.name} fetches a ball")

class cat(animal):
    def purr(self):
        print(f"{self.name}purss.....")

d = dog("binni")
d.speak()
d.fetch()

class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)


# Creating objects
tom = Robot("Tom")
jerry = Robot("Jerry")

# Robots introduce themselves
tom.introduce()
jerry.introduce()

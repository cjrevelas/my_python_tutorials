class Animal:
    def __init__(self, name: str, legs: int):
        self.name_ = name
        self.legs_ = legs

    def Speak(self):
        print("Just a random animal speaking")

    def Identify(self):
        print("Just a random animal identifying")


class Dog(Animal):
    def __init__(self, name: str, legs: int):
        super().__init__(name, legs)

    def Speak(self):
        print("Woof woof")
        return

    def Identify(self):
        print("I am a dog!")
        print("My name is " + self.name_)
        print("I have " + str(self.legs_) + " legs\n")
        return


class Cat(Animal):
    def __init__(self, name: str, legs: int):
        super().__init__(name, legs)

    def Speak(self):
        print("Meow!")
        return

    def Identify(self):
        print("I am a cat!")
        print("My name is " + self.name_)
        print("I have " + str(self.legs_) + " legs\n")
        return


myDog = Dog("sandy", 4)
myDog.Speak()
myDog.Identify()

myCat = Cat("mitsos", 4)
myCat.Speak()
myCat.Identify()

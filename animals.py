# we want to define two classes named Dog and Cat.
# Each of those classes will have the following attributes:
    # name: str
    # legs: int
# and the following methods:
    # __init__(self, ...)   [will initialize the name and legs of self]
    # speak(self,...)       [Dog objects will print "Woof Woof", Cat objects will print "Meow"]
    # identify(self,...)    [will print name of animal and number of legs]

# create a Dog object myDog with name "sandy" and legs = 4
# create a Cat object myCat with name "mitsos" and legs = 4

class Dog:
    def __init__(self, inputName: str, inputLegs: int):
        self.name = inputName
        self.legs = inputLegs

    def speak(self):
        print("Woof woof!")
        return

    def identify(self):
        print("I am a dog!")
        print("My name is " + self.name)
        print("I have " + str(self.legs) + " legs\n")
        return


class Cat:
    def __init__(self, inputName: str, inputLegs: int):
        self.name = inputName
        self.legs = inputLegs

    def speak(self):
        print("Meow!")
        return

    def identify(self):
        print("I am a cat!")
        print("My name is " + self.name)
        print("I have " + str(self.legs) + " legs\n")
        return


myDog = Dog("sandy", 4)
myDog.speak()
myDog.identify()

myCat = Cat("mitsos", 4)
myCat.speak()
myCat.identify()

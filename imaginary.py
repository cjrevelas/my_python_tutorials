'''
As we use a function by calling it from another function,
we "use" the functionality of a class by creating/constructing
an object of the class.

The variables associated with an object of the class are also called "attributes".
The functions associated with an object of the class are also called "methods".

To create an object we use a special method of the class, its "constructor".
In Python, the constructor is always named as "__init__".

We can think of a class as a new and custom data type, and its objects
as variables of this custom data type.

Every attribute and method defined inside the class needs the self
keyword, so that the interpreter can know which object the functionality
of the class must be performed on. Thus, every variable/attribute needs
a "self" prefix and the first argument of every method must be the "self" object.

Below we define a class for a custom representation of a complex
number.
To construct an object of class Complex, named x,
we use the constructor of the class, i.e., the method __init__(...)
passing it two float numbers.
'''

class Complex:
    def __init__(self, inputNumber1: float, inputNumber2: float):
        print("message: creating a new object of class Complex")
        self.realPart = inputNumber1
        self.imagPart = inputNumber2

    def PrintNumber(self, string: str):
        print("the number is " + str(self.realPart) + " + " + str(self.imagPart) + string)

    def SumParts(self) -> float:
        return self.realPart + self.imagPart

def main() -> None:
    x = Complex(2.0, 3.0) # calls __init__ of Complex with self = x
    y = Complex(5.0, 4.0) # calls __init__ of Complex with self = y

    print("Real part of x: "      + str(x.realPart))
    print("Imaginary part of x: " + str(x.imagPart))

    print("Real part of y: "      + str(y.realPart))
    print("Imaginary part of y: " + str(y.imagPart))

    x.PrintNumber(": x object")
    y.PrintNumber(": y object")

    theSumOfPartsOfX = x.SumParts()
    print(theSumOfPartsOfX)

    theSumOfPartsOfY = y.SumParts()
    print(theSumOfPartsOfY)

if __name__ == "__main__":
    main()

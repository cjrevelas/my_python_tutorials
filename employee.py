class Employee:
    def __init__(self, inputName: str, inputAge: int, inputSalary: float):
        self.name   = inputName
        self.age    = inputAge
        self.salary = inputSalary

    def work(self) -> None:
        print(self.name + " is now working..\n")
        return

    def timeOut(self) -> None:
        print(self.name + " is now on a break..\n")
        return

    def printInfo(self) -> None:
        print(self.name + " is " + str(self.age) + " years old and gets " + str(self.salary) + " per month :)\n")
        return


def main():
    constantinos = Employee("constantinos", 42, 1500.10)
    katerina     = Employee("katerina", 32, 2400.50)

    print("\n")

    katerina.printInfo()
    constantinos.printInfo()

    katerina.work()
    constantinos.timeOut()

    constantinos.work()
    katerina.timeOut()


main()

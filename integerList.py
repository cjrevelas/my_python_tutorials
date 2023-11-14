from typing import List

class IntegerList:
    def __init__ (self, inputList: List[int]):
        self.list = inputList
        print(self.list)

    def FindProduct(self) -> int:
        product = 1

        for ii in self.list:
            product *= ii
            print(product)

        return product

    def MultiplyBy(self, multiplier: int) -> List[int]:
        multipliedList = list()

        for ii in self.list:
            multipliedList.append(ii*multiplier)

        return multipliedList

    def FindEvenNumberss(self) -> List[int]:
        evenList = list()

        for ii in self.list:
            if (ii % 2 == 0):
                evenList.append(ii)

        return evenList


def main():
    myList = IntegerList([1, 2, 15, 1, 22])

    print(myList.FindProduct())
    print('\n')

    print(myList.MultiplyBy(3))
    print('\n')

    print(myList.FindEvenNumberss())
    print('\n')


main()

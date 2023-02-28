"""
HERE, WE DEMONSTRATE HOW TO DEFINE AND USE A FUNCTION IN PYTHON
"""

"""
We define a function by defining its signature and its body.
function signature: name + arguments/parameters + return type
function body: all statements that are executed inside the function

def function_name(function_arguments: type_of_function_arguments) -> return_type:
    ..blah..
    ..more statements..

    return (...)
"""
from typing import List


'''
Define a function that simply prints a string.
'''
def MyPrint(myString: str) -> None: # Definition of function "myPrint()"
  print(myString)
  return


'''
Define a function that returns the sum of two integers.
'''
def MySum(x: int, y: int) -> int:
    return (x+y) # it becomes clear here, that the return statement is also a part of the function body
                 # in fact, functions performing trivial operations (like this one) can comprise just one return statement


'''
Define a function that receives an integer and returns the sum of all positive
integers smaller than that integer.
'''
def SumOfNumbers(y: int) -> int:
    summ = 0

    for ii in range(0,y,1):
        summ += ii

    return summ


'''
Define a function with name SumOfList, which will receive a list of floats
and returns their sum.
'''
def SumOfList(inputList: List[float]) -> float:
    summ = 0.0

    for number in inputList:
        summ += number

    return summ


'''
Define a funciton with name EvenProduct, which will receive two integers and
check whether their product is an even number.
'''
def EvenProduct(x: int, y: int) -> bool:
    product = x*y
    isEven  = (product % 2 == 0)

    return isEven


'''
Define a function with name ListOfSquares, which will receive a list of integers,
and returns a new List containing the squares of those numbers.
'''
def ListOfSquares(inputList: List[int]) -> List[int]:
    newList = list()

    for number in inputList:
        newList.append(number**2)

    return newList


'''
Define a function with name ListOfEvenNumbers, which will receive a list of integers,
and returns a new list containing only the even of those integers.
'''

'''
main() function
'''
def main(): # Definition of function "main()", which is the central function of a python script
    myString = "This is my first function in Python!"
    MyPrint(myString)
    print("\n")

    x = 2
    y = 5
    z = MySum(x,y)
    print(z)
    print("\n")

    x = SumOfNumbers(10)
    print(x)
    print("\n")

    print(EvenProduct(3,7))
    print("\n")

    y = SumOfList([2.0, 3.4, 2.98, 8.7, 6.5, 9.2])
    print(y)
    print("\n")

    print(ListOfSquares(range(1,11)))

    return


main() # At this point we call function "main()" and execution of the script starts.

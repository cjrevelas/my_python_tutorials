"""
HERE, WE DEMONSTRATE HOW TO DEFINE AND USE A FUNCTION IN PYTHON
"""

"""
We define a function by defining its signature and its body
function signature: name + arguments/parameters + return type
function body: all statements that are executed inside the function

def function_name(function_arguments: type_of_function_arguments) -> return_type:
    ..blah..
    ..more statements..
    
    return (...)
"""

def myPrint(myString: str) -> None: # Definition of function "myPrint()"
  print(myString)
  return
    
def mySum(x: int, y: int) -> int:
    return (x+y) # it becomes clear here, that the return statement is also a part of the function body
                 # in fact, functions performing trivial operations (like this one) can comprise just one return statement

def main(): # Definition of function "main()", which is the central function of a python script
  myString = "This is my first function in Python!\n"
  myPrint(myString) # At this point we call function "myPrint()"
  return


main() # At this point we call function "main()", which in turn will call function "myPrint()"

x = 2
y = 5

z = mySum(x,y)

for i in range(10):
  print(mySum(i,x))

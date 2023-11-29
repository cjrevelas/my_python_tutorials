import numpy as np
import time
import sys

'''
The main object of Numpy (Numerical Python) is a multidimensional array.

This array contains elements of the same type indexed by a tuple of positive integers.

In the context of Numpy, we refer to array dimensions as "axes".
'''

def main() -> None:
    print("Hello")

    # Basic numpy array initialization syntax
    a = np.array([1,2,3])
    print(a)

    # Comparing a numpy array to a python list
    b = range(1000)
    print(sys.getsizeof(5) * len(b))

    c = np.arange(1000)
    print(c.itemsize * c.size)

    size = 100000

    
    l1  = range(size)
    l2  = range(size)
    rs1 = [None] * size

    n1 = np.arange(size)
    n2 = np.arange(size)
   
    startTime = time.time()

    for ii in range(size):
        rs1[ii] = l1[ii] + l2[ii]

    endTime = time.time()

    print("python list addition time (ms): ", (endTime - startTime) * 1000)

    startTime = time.time()

    rs2 = n1 + n2
    
    endTime = time.time()
    
    print("numpy array addition time (ms): ", (endTime - startTime) * 1000)

    # Let's work with our first 2d array
    a = np.array([[4,7], [2,8], [5, 6]])
    print(a)
    print(a.ndim) # number of axes/dimensions
    print(a.itemsize)
    print(a.shape) # number of elements along each axis/dimension

    a = np.array([[4,7], [2,8], [5, 6]], dtype=np.float32)
    print(a.itemsize)

    a = np.array([[4,7], [2,8], [5, 6]], dtype=np.float64)
    print(a)
    print(a.itemsize)

    a = np.array([[4,7], [2,8], [5, 6]], dtype=complex)
    print(a)
    print(a.itemsize)

    # Initialization of a numpy array of a certain shape
    a = np.zeros((3,4))
    print(a)

    a = np.zeros((3,4), dtype = int)
    print(a)

    a = np.ones((3,4))
    print(a)

    a = np.arange(10)
    print(a)

if __name__ == "__main__":
    main()

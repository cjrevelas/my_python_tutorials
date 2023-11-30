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
    print()

    # Comparing a numpy array to a python list
    b = range(1000)
    print(sys.getsizeof(5) * len(b))
    print()

    c = np.arange(1000)
    print(c.itemsize * c.size)
    print()

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
    print()

    startTime = time.time()

    rs2 = n1 + n2

    endTime = time.time()

    print("numpy array addition time (ms): ", (endTime - startTime) * 1000)
    print()

    # Let's work with our first 2d array
    a = np.array([[4,7], [2,8], [5, 6]])
    print(a)
    print(a.ndim) # number of axes/dimensions
    print(a.itemsize)
    print(a.shape) # number of elements along each axis/dimension
    print()

    a = np.array([[4,7], [2,8], [5, 6]], dtype=np.float32)
    print(a.itemsize)
    print()

    a = np.array([[4,7], [2,8], [5, 6]], dtype=np.float64)
    print(a)
    print(a.itemsize)
    print()

    a = np.array([[4,7], [2,8], [5, 6]], dtype=complex)
    print(a)
    print(a.itemsize)
    print()

    # Initialization of a numpy array of a certain shape
    a = np.zeros((3,4))
    print(a)
    print()

    a = np.zeros((3,4), dtype = int)
    print(a)
    print()

    a = np.ones((3,4))
    print(a)
    print()

    a = np.arange(10)
    print(a)
    print()

    # Reshaping an array
    a = np.arange(9)
    print(a)

    b = a.reshape(3,3)
    print(b)
    print()

    c = b.flatten()
    print(c)

    c = b.flatten(order='F')
    print(c)
    print()

    d = np.arange(20).reshape(4,5)
    print(d)
    print()

    k = np.transpose(d)
    print(k)
    print()

    a = np.arange(8).reshape(2,4)
    print(a)
    print()

    b = a.reshape(2,2,2)
    print(b)
    print()

    x = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
    print(x)
    print()

    print(np.swapaxes(x,0,2))
    print()

if __name__ == "__main__":
    main()

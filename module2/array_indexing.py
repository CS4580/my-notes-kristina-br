
#print(__name__)
"""Array indexing
"""
import numpy as np

def main():
    """Driven Function
    """

    arr_1d = np.arange(10)
    #Access the second element. Index notation
    print(arr_1d[1])
    # Last element
    print(arr_1d[-1])

    # Access 2D array elements
    arr_2d = np.array([[21, 22, 23, 24],
              [31, 32, 33, 34],
              [41, 42, 43, 44]])


if __name__ == '__main__':
    main() # if the value is = to main then call this entry point
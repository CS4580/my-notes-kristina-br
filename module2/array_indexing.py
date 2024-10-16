
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
    print(f'The 0,0 element {arr_2d[0,0]}')
    print(f'The 2, -2 element {arr_2d[2,-2]}')
    print(f'Full first row {arr_2d[0]}')

    # slicing :p
    arr_1d = np.arange(10)
    




if __name__ == '__main__':
    main() # if the value is = to main then call this entry point
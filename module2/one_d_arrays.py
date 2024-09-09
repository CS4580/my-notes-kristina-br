
#print(__name__)
"""_summary_
"""

import numpy as np

def main():
    """Driven Function
    """
    # create an array
    array = np.array([-2, 1, -5, 10])
    print(array, type(array))

    numbers = [-2, 1, -5, 10]
    print(numberrs, type(numbers))
    # convert list into arrays
    new_array = np.array(numbers)
    print(new_array)

    # 2D Arrays
    matrix = np.array([[-1, 0, 4], [-3, 6, 9]])
    print(matrix)
    # 3D Arrays
    array3d = np.array([[[-1, 2, 3],
                [3, 5, 7],
                [4, 6, 8]
                [3, 2, 5]]
            ])
    print(f'3D array {array3d}')

    # use the dtype optional argument to explicitly
    # call the data type of  the array
    numbers = [-2, 1, -5, 10]
    new_array = np.array(numbers, dtype=np.short)
    print(new_array, new_array.dtype)
    

if __name__ == '__main__':
    main() # if the value is = to main then call this entry point
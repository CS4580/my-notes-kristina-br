
#print(__name__)
<<<<<<< HEAD
"""1D Arrays
"""
=======
"""_summary_
"""

>>>>>>> 83ab7bbcd2474c32f354f42e6bab384b6cda41d1
import numpy as np

def main():
    """Driven Function
    """
<<<<<<< HEAD
    print('Main function')
=======
    # create an array
    array = np.array([-2, 1, -5, 10])
    print(array, type(array))

    numbers = [-2, 1, -5, 10]
    print(numbers, type(numbers))
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
    # unsigned data
    pos_numbers = [2, 1, 5, 10]
    new_array = np.array(pos_numbers, dype=np.ushort) 
    #ushort = unsigned short
    print(new_array, new_array.dtype)
    # FLoat data
    new_array = np.array(pos_numbers, dtype=np.float32)
    print(new_array, new_array.dtype)
>>>>>>> 83ab7bbcd2474c32f354f42e6bab384b6cda41d1

if __name__ == '__main__':
    main() # if the value is = to main then call this entry point
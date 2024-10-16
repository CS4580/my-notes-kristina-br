
#print(__name__)
"""Practice some of the numpy array identities
"""

import numpy as np

def main():
    """Driven Function
    """
    # Create a 2D 3x3 identity matrix
    identity_3x3 = np.eye(3,3)
    print(identity_3x3)

    identity_3x5 = np.eye(3,5)
    print(identity_3x5)
    # 2D Diagonal Arrays, with given entries
    diagonal_2D = np.diag([2, 3, 4, 5])
    print(diagonal_2D)

    # Create a 5x3 2D array of unsigned integers filled with zeros
    arr_5x3_zeros = np.zeros((5,3), dtype=np.uint)
    print(f'arr_5x3_zeros {arr_5x3_zeros}')
    # Create a 5x3 2D array of unsigned integers filled with ones
    arr_5x5_ones = np.ones((5,3), dtype=np.uint)
    print(f'arr_5x5_ones {arr_5x5_ones}')

    # Create a 5x3 2D array of unsigned integers filled w/ another value
    arr_5x3_pi = np.full((5,3), np.pi) # 2nd arg is what vals to fill instead of type
    print(f'arr_5x3_pi {arr_5x3_pi}')


if __name__ == '__main__':
    main() # if the value is = to main then call this entry point
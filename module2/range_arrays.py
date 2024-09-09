"""Practice creating arrays from ranges
"""

import numpy as np

def main():
    """Driven Function
    """
    # Generate 1D arrays from 0 to 8
    array = np.arange(9)
    print(array)
    # you may have negative numbers
    array = np.arange(-8, 8, 2)
    print(array)

    #Generate an array with values from 0 to 5, in steps of 0.1
    array = np.arange(0, 5, 0.2)
    print(array)
    # Ranges with decimal values
    array = np.arange(0.1, 0.3, 0.01)
    print(array)


if __name__ == '__main__':
    main() # if the value is = to main then call this entry point
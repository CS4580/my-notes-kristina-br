
#print(__name__)
"""_summary_
"""

import numpy as np

def main():
    """Driven Function
    """
    numbers_lst = [2, 4, 5, 8, 10]
    print(f'Before list{numbers_lst}')
    # Increment each element by 3
    for item in range(len(numbers_lst)):
        numbers_lst[item] = numbers_lst[item] + 3
    print(f'After list {numbers_lst}')
    # Convert list to a Numpy array
    numbers_arr = np.array(numbers_lst)
    print(f'Before array {numbers_arr}')
    # Add 3 to each element
    numbers_arr += 3
    print(f'After array {numbers_arr}')

if __name__ == '__main__':
    main() # if the value is = to main then call this entry point
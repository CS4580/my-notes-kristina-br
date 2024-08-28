#print(__name__)
"""Library to calculate number of digits
for differet algorithms
"""
import math

def factorial_length(number):
    """Count the number of digits in a factorial number

    Args:
        number (int): integer value to calculate factorial

    Returns:
        int: number of digits for factorial of input
    """
    number = math.factorial(number)
    length = str(number)
    return len(length)
#    while number >= 1:
 #       number / 10
  #      length = length + 1


def main():
    """Driven Function
    """
    number = 5
    digits = factorial_length(number)
    print(f'You have {digits} in factorial({number})')

if __name__ == '__main__':
    main() # if the value is = to main then call this entry point
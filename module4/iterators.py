"""Iterator protocols
"""

def main():
    """Driven Function
    """
    iterable = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    # create an iterator
    iterator = iter(iterable)
    # get 1st element
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator)) # call it any more any you'll get kind of a null ptr error

    # TODO: Add a function with a try: catch: to test the iterator

    # TODO: Then use a Generator.

if __name__ == '__main__':
    main() # if the value is = to main then call this entry point
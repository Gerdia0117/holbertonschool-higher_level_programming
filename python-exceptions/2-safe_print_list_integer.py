#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list, only integers.

    Args:
        my_list (list): List to print from.
        x (int): Number of elements to access.

    Returns:
        int: Number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            raise
    print()
    return count

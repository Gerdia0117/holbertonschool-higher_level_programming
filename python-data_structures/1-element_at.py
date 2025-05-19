#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list at a given index."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    # Test with valid indices
    print("Element at index 0: {}".format(element_at(my_list, 0)))
    print("Element at index 2: {}".format(element_at(my_list, 2)))
    print("Element at index 4: {}".format(element_at(my_list, 4)))
    # Test with invalid indices
    print("Element at index -1: {}".format(element_at(my_list, -1)))
    print("Element at index 5: {}".format(element_at(my_list, 5)))

def multiply(value1, value2):
    """
    This method is used to multiply two values and return the result
    :param value1: integer value 1
    :param value2: integer value 2
    :return: value after multiplying
    """
    return value1 * value2

import os


def get_path(filename):
    """Return file's path or empty string if no path."""
    head, tail = os.path.split(filename)
    import pdb; pdb.set_trace()
    return head


filename = __file__
print(f'path = {get_path(filename)}')
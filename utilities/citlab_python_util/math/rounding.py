def round_to_nearest_integer(x):
    """ Round the value x to the nearest integer. This method is necessary since in Python 3 the builtin
    round() function is performing Bankers rounding, i.e. rounding to the nearest even integer value.

    :param x: value to be rounded
    :type x: Union[int, float]
    :return: the closest integer to x
    """
    if x % 1 >= 0.5:
        return int(x) + 1
    else:
        return int(x)

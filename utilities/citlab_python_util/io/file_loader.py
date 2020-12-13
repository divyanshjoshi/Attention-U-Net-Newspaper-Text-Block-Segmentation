def load_text_file(filename):
    """ Load text file ``filename`` and return the (stripped) lines as list entries.

    :param filename: path to the file to be loaded
    :type filename: str
    :return: list of strings consisting of the (stripped) lines from filename
    """
    res = []

    with open(filename, 'r') as f:
        for line in f:
            if line == "\n":
                res.append(line)
            else:
                res.append(line.strip())

        return res

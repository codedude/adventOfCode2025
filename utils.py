import os


def read_file(filename):
    if not os.path.isfile(filename):
        print('File does not exist.')
        return None
    with open(filename, 'r') as f:
        return f.read()


def read_lines(filename):
    content = read_file(filename)
    if content is not None:
        return content.splitlines()
    else:
        return None

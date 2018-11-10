import os


def get_path(file_path):
    tail, head = os.path.split(file_path)
    return tail, head


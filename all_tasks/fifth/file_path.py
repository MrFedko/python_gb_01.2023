import os


def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension

from make_files import make_files


def new_make_file(extensions: dict):
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)

import os

# keyword = 'check_async_unsafe'  # ask the user for keyword, use raw_input() on Python 2.x


def search_fun_dir(root_dir, keyword):
    # root_dir = "/Users/tshi/researchProjs/django/django-3.2.14/"  # path to the root directory to search
    existent = []
    for root, dirs, files in os.walk(root_dir, onerror=None):  # walk the root dir
        for filename in files:  # iterate over the files in the current dir
            file_path = os.path.join(root, filename)  # build the file path
            try:
                with open(file_path, "rb") as f:  # open the file for reading
                    # read the file line by line
                    for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                        try:
                            line = line.decode("utf-8")  # try to decode the contents to utf-8
                        except ValueError:  # decoding failed, skip the line
                            continue
                        if keyword in line:  # if the keyword exists on the current line...
                            # print(file_path)  # print the file path
                            existent.append(file_path)
                            break  # no need to iterate over the rest of the file
            except (IOError, OSError):  # ignore read and permission errors
                pass
    return existent



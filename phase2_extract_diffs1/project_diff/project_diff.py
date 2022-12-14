import os
from fnmatch import fnmatch
from phase2_extract_diffs1.project_diff.constant import ignores_ext, ignores


class example:
    pass


# def file_list_by_type(root, ptn):
#     ls = []
#     for path, subdirs, files in os.walk(root):
#         for name in files:
#             if fnmatch(name, ptn):
#                 ls.append(os.path.join(path, name))
#     return ls


def get_all_files(base_dir):
    ls = []
    for path, subdirs, files in os.walk(base_dir):
        for name in files:
            if fnmatch(name, '*'):
                ls.append((path, name))
    return ls


def get_workable_files(base_dir):
    file_ls = get_all_files(base_dir)
    work_file_ls = []

    for pyf in file_ls:
        if pyf[1].endswith(".py"):
            if 'test' not in pyf[0]:
                if 'doc' not in pyf[0]:
                    if 'example' not in pyf[0]:
                        if pyf[1] not in ignores:
                            relative_path = pyf[0].removeprefix(base_dir)
                            work_file_ls.append((relative_path, pyf[1]))
    return work_file_ls

import re, os

from breachin.project_diff.file_diff import build_file_path, output_file_diff, output_file_diff_with_file_name
from breachin.project_diff.project_diff import get_workable_files
from breachin.project_diff.search_str_dir import search_fun_dir
from regex import func_sig, class_sig, class_sig_param

old_base_dir = '/Users/tshi/researchProjs/scipy/scipy-1.3.0/'
new_base_dir = '/Users/tshi/researchProjs/scipy/scipy-1.8.0/'

if __name__ == '__main__':
    old_ver_ls = get_workable_files(old_base_dir)
    new_ver_ls = get_workable_files(new_base_dir)

    removed_f = []
    added_f = []
    remained_f = []
    remained_full_path_old = []
    remained_full_path_new = []

    for f in old_ver_ls:
        if f not in new_ver_ls:
            removed_f.append(f)
        else:
            remained_f.append(f)

    for f in new_ver_ls:
        if f not in old_ver_ls:
            added_f.append(f)

    diffs = []
    for rf in remained_f:
        diffs = output_file_diff_with_file_name(old_base_dir, new_base_dir, rf)

    # for d in diffs:
    #     print(d)

    # print('added file ' + str(len(added_f)))
    # print(added_f)
    # print('removed file ' + str(len(removed_f)))
    # print(removed_f)
    # print('unchanged file ' + str(len(remained_f)))
    # print(remained_f)

    added_module = []
    removed_module = []
    moved_module = []

    for f in added_f:
        filename = build_file_path(new_base_dir, f)
        with open(filename, 'r') as my_file:
            filetext = my_file.read()
            if 'class' in filetext or 'def' in filetext:
                added_module.append(f)


    for f in removed_f:
        filename = build_file_path(old_base_dir, f)
        with open(filename, 'r') as my_file:
            filetext = my_file.read()
            if 'class' in filetext or 'def' in filetext:
                removed_module.append(f)

    added_filename = []
    removed_filename = []
    for f in added_module:
        added_filename.append(f[1])

    for f in removed_module:
        removed_filename.append(f[1])

    moved_module = list(set(added_filename).intersection(removed_filename))

    print('added module ' + str(len(added_module)))
    # print(added_module)
    print('removed module ' + str(len(removed_module)))
    # print(removed_module)
    print('moved module ' + str(len(moved_module)))
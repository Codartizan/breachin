import re

from breachin.project_diff.file_diff import build_file_path
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
    removed_full_path = []
    added_full_path = []

    for f in old_ver_ls:
        if f not in new_ver_ls:
            removed_f.append(f)
        else:
            remained_f.append(f)

    for f in new_ver_ls:
        if f not in old_ver_ls:
            added_f.append(f)

    for r in removed_f:
        removed_full_path.append(build_file_path(old_base_dir, r))

    for a in added_f:
        added_full_path.append(build_file_path(new_base_dir, a))

    removed_func = []
    removed_class = []

    for rf in removed_full_path:
        with open(rf) as file:
            for line in file:
                func = re.search(func_sig, line)
                if func:
                    removed_func.append((rf, line.removesuffix('\n')))
                clas = re.search(class_sig, line)
                if clas:
                    removed_class.append((rf, line.removesuffix('\n')))
                clas_p = re.search(class_sig_param, line)
                if clas_p:
                    removed_class.append((rf, line.removesuffix('\n')))

    print('Removed functions {} and classes {}:'.format(len(removed_func), len(removed_class)))
    print(removed_func)
    print(removed_class)

    moved_func = []
    moved_clas = []

    for rfn in removed_func:
        if len(search_fun_dir(new_base_dir, rfn[1])) > 0:
            moved_func.append(rfn)

    for rcl in removed_class:
        if len(search_fun_dir(new_base_dir, rcl[1])) > 0:
            moved_clas.append(rcl)

    print('Moved functions {} and classes {}:'.format(len(moved_func), len(moved_clas)))
    print(moved_func)
    print(moved_clas)

    modified_func = []
    modified_clas = []

    for rfn in removed_func:
        if re.match(func_sig, rfn[1]) is not None and rfn not in moved_func:
            sig = 'def ' + re.match(func_sig, rfn[1]).group(1)
            if len(search_fun_dir(new_base_dir, sig)) > 0:
                modified_func.append(rfn)

    for rcl in removed_class:
        clazz = re.match(class_sig_param, rcl[1].lstrip()) if '(' in rcl[1] and ')' in rcl[1] else re.match(class_sig, rcl[1].lstrip())
        if clazz is not None and rcl not in moved_clas:
            clazz_sig = 'class ' + clazz.group(1)
            if len(search_fun_dir(new_base_dir, clazz_sig)) > 0:
                modified_clas.append(rcl)

    print('Modified functions {} and classes {}:'.format(len(modified_func), len(modified_clas)))
    print(modified_func)
    print(modified_clas)

    added_func = []
    added_class = []

    for af in added_full_path:
        with open(af) as file:
            for line in file:
                func = re.search(func_sig, line)
                m = re.match(func_sig, line)
                if func and m is not None:
                    func_sig = m.group(1)
                    if len(search_fun_dir(old_base_dir, func_sig)) > 0:
                        added_func.append((af, line.removesuffix('\n')))
                clazz = re.match(class_sig_param, af[1].lstrip()) if '(' in af[1] and ')' in af[1] else re.match(
                    class_sig, af[1].lstrip())
                if clazz is not None:
                    clazz_sig = clazz.group(1)
                    if len(search_fun_dir(old_base_dir, clazz_sig)) > 0:
                        added_class.append((af, line.removesuffix('\n')))

    print('Added functions {} and classes {}'.format(len(added_func), len(added_class)))
    print(added_func)
    print(added_class)

    print('In total: \n'
          'Removed function {}, class {} \n'
          'Moved function {}, class {} \n'
          'Modified function {}, class {} \n'
          'Added function {}, class {}'. format(len(removed_func)-len(moved_func)-len(modified_func), len(removed_class)-len(moved_clas)-len(modified_clas),
                                                len(moved_func), len(moved_clas), len(modified_func), len(modified_clas),
                                                len(added_func), len(added_class)))

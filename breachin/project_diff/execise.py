from breachin.project_diff.project_diff import get_workable_files

old_base_dir = '/Users/tshi/researchProjs/django/django-2.2/'
new_base_dir = '/Users/tshi/researchProjs/django/django-3.2.14/'

if __name__ == '__main__':
    old_ver_ls = get_workable_files(old_base_dir)
    new_ver_ls = get_workable_files(new_base_dir)

    removed_f = []
    added_f = []
    remained_f = []

    for f in old_ver_ls:
        if f not in new_ver_ls:
            removed_f.append(f)
        else:
            remained_f.append(f)

    for f in new_ver_ls:
        if f not in old_ver_ls:
            added_f.append(f)

    for i in remained_f:
        print(i)


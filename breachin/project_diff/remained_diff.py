from breachin.project_diff.file_diff import output_file_diff_with_file_name
from breachin.project_diff.project_diff import get_workable_files

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

    print(len(remained_f))

    with open(r'/Users/tshi/PycharmProjects/breachin/breachin/output/remained_diff.txt', 'w') as fp:
        diffs = []
        for rf in remained_f:
            diffs = output_file_diff_with_file_name(old_base_dir, new_base_dir, rf)
            if len(diffs) > 0:
                fp.write("%s\n" % str(rf))
                for d in diffs:
                    fp.write("%s\n" % d)

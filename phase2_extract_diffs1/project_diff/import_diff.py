from phase2_extract_diffs1.project_diff.project_diff import get_workable_files
from phase2_extract_diffs1.project_diff.file_diff import output_file_diff
from phase2_extract_diffs1.project_diff.constant import new_base_dir, old_base_dir
import re
from regex import imports, imports2


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
    add = 0
    rem = 0
    out = []
    for rf in remained_f:
        diffs = output_file_diff(old_base_dir, rf, new_base_dir, rf)
        for diff in diffs:
            match = re.search(imports, diff)
            if match is not True:
                match = re.search(imports2, diff)
            if match:
                out.append(str(rf))
                out.append(diff)
                if diff.startswith('+'):
                    add += 1
                if diff.startswith('-'):
                    rem += 1

    '''
        关于import，先确定每个文件有多少个不同，如果-+数量相同，则比较similarity，然后算出多少修改，多少添加，多少减少
        关于function看空格来决定function是不是结束
    '''
    with open(r'/phase2_extract_diffs1/output/import_diff.txt', 'w') as fp:
        for item in out:
            # write each item on a new line
            fp.write("%s\n" % item)

    print(add)
    print(rem)
    print(add + rem)

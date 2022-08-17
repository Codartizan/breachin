import difflib


def output_file_diff(old_base_dir, old_file, new_base_dir, new_file):

    old_f_path = build_file_path(old_base_dir, old_file)
    new_f_path = build_file_path(new_base_dir, new_file)

    with open(old_f_path) as file_1:
        file_1_text = file_1.readlines()

    with open(new_f_path) as file_2:
        file_2_text = file_2.readlines()

    # Find and print the diff:
    for line in difflib.unified_diff(file_1_text, file_2_text, fromfile=old_base_dir, tofile=new_base_dir, lineterm=''):
        print(line)


def build_file_path(base_dir, file_tuple):
    if file_tuple[0] == '':
        return base_dir + file_tuple[1]
    else:
        return base_dir + file_tuple[0] + '/' + file_tuple[1]


old_dir = '/Users/tshi/researchProjs/django/django-2.2/'
new_dir = '/Users/tshi/researchProjs/django/django-3.2.14/'

newf = ('', 'setup.py')
oldf = ('', 'setup.py')

output_file_diff(old_dir, oldf, new_dir, newf)
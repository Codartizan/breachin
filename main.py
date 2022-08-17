# This is a sample Python script.
from breachin.libraries_io_api.get_dependencies_by_rank import search_dependency_by_rank
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dependencies = search_dependency_by_rank()

    for d in dependencies:
        print(d.name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

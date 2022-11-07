from phase2_extract_diffs1.libraries_io_api.get_dependencies_by_rank import search_dependency_by_rank
from phase2_extract_diffs1.libraries_io_api.get_source_rank import get_dep_source_rank

dependencies = search_dependency_by_rank()

print(len(dependencies))

for dep in dependencies:
    dependency_name = dep.name
    print(dependency_name)
    # source_rank = get_dep_source_rank(dependency_name)
    # if source_rank.versions_present == 1 and \
    #         source_rank.recent_release == 1 and \
    #         source_rank.not_brand_new == 1 and \
    #         source_rank.one_point_oh == 1 and \
    #         source_rank.is_deprecated == 0:
    #     print(dependency_name)


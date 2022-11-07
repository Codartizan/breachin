from src.dependency.search_dep import search_dependency_by_rank, find_research_version
from src.dependent.dep_filter import find_target_version
from src.util.util import repo_full_name

dependencies = search_dependency_by_rank()

ver_obj = []

for d in dependencies:
    dependency_name = d.name
    dependency_full_name = repo_full_name(d.repository_url)

    for v in d.versions:
        pub_date = v.published_at[0:10]
        ver_obj.append((v.number, pub_date))

    ver_obj.sort(key=lambda y: y[1], reverse=True)

    print(dependency_name)
    # print(ver_obj)
    # print("======================")


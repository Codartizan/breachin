# import base64
# import os
#
# from loguru import logger
#
# from src.dependent.code_search import dep_appearance, file_dep_appearance, count_appearance
# from src.dependent.dep_filter import has_content, \
#     extract_dependency_version
# from src.util.util import write_if_not_exist, mapping_resp_to_generic
#
#
# def test_rerun_failed():
#     path = '/Users/tshi/PycharmProjects/softeng795/docs/{}'
#     # list_dir = os.listdir(path)
#     #
#     # for i in list_dir:
#     #     if i.endswith('.txt') is not True:
#     #         dep = i
#     dep = 'matplotlib'
#     dep_path = path.format(dep)
#     dep_dir = os.listdir(dep_path)
#     for r in dep_dir:
#         if r.startswith('Failed-'):
#             file_path = dep_path + '/' + r
#             logger.info('Now working on file {}'.format(file_path))
#             dependents = []
#             with open(file_path) as file:
#                 while line := file.readline().rstrip():
#                     dependents.append(line)
#             for d in dependents:
#                 if write_if_not_exist(dep, d):
#                     code_search_resp = dep_appearance(dep, d)
#
#                     if code_search_resp.status_code == 200:
#                         appr = count_appearance(code_search_resp, dep, d)
#                         has_req = file_dep_appearance(code_search_resp, 'requirements.txt')
#                         has_setup = file_dep_appearance(code_search_resp, 'setup.py')
#
#                         if appr > 2:
#                             pkg_file = 'requirements.txt'
#                             if has_req:
#                                 pkg_file = 'requirements.txt'
#                             elif not has_req and has_setup:
#                                 pkg_file = 'setup.py'
#                             elif has_req and has_setup:
#                                 pkg_file = 'requirements.txt'
#
#                             pkg_management_file_resp = has_content(d, pkg_file)
#
#                             if pkg_management_file_resp.status_code == 200:
#                                 res_obj = mapping_resp_to_generic(pkg_management_file_resp)
#                                 pkg_management_decoded_content = base64.b64decode(res_obj.content).decode()
#                                 found_version = extract_dependency_version(pkg_management_decoded_content,
#                                                                            dep)
#                                 logger.debug('{} is using {} version {}'.format(d, dep, found_version))
#                                 write_if_not_exist('{}-{}'.format(dep, found_version),
#                                                    '{} | {} | {}'.format(d, res_obj.name, appr))
#
#                     elif code_search_resp.status_code == 403:
#                         write_if_not_exist('Failed-{}'.format(dep), d)

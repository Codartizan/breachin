import base64

from loguru import logger

from src.dependency.search_dep import search_dependency_by_rank
from src.dependent.code_search import dep_appearance, file_dep_appearance, count_appearance
from src.dependent.dep_filter import find_target_version, has_content, \
    extract_dependency_version, has_pytest
from src.dependent.dep_scraper import scraping_dependent_pkg
from src.util.util import repo_full_name, write_if_not_exist, mapping_resp_to_generic


def test_phase_one():
    dependencies = search_dependency_by_rank()
    dependency = dependencies[12]
    dependency_name = dependency.name
    dependency_full_name = repo_full_name(dependency.repository_url)
    target_version = find_target_version(dependency)
    logger.debug('Target dependency full name - {}'.format(dependency_full_name))

    prop_dependents = []
    suffix = ''
    counter = 0
    while len(prop_dependents) < 20:
        counter += 1
        logger.debug('Scraping on page round {}'.format(counter))
        dependents_tuple = scraping_dependent_pkg(dependency_full_name, suffix)
        suffix = dependents_tuple[1]

        for d in dependents_tuple[0]:
            if write_if_not_exist(dependency_name, d):
                code_search_resp = dep_appearance(dependency_name, d)
                has_test = False
                ver_match = False

                if code_search_resp.status_code == 200:
                    appr = count_appearance(code_search_resp, dependency_name, d)
                    has_req = file_dep_appearance(code_search_resp, 'requirements.txt')
                    has_setup = file_dep_appearance(code_search_resp, 'setup.py')

                    if appr > 2:
                        pkg_file = 'requirements.txt'
                        if has_req:
                            pkg_file = 'requirements.txt'
                        elif not has_req and has_setup:
                            pkg_file = 'setup.py'
                        elif has_req and has_setup:
                            pkg_file = 'requirements.txt'

                        pkg_management_file_resp = has_content(d, pkg_file)

                        if pkg_management_file_resp.status_code == 200:
                            res_obj = mapping_resp_to_generic(pkg_management_file_resp)
                            pkg_management_decoded_content = base64.b64decode(res_obj.content).decode()
                            found_version = extract_dependency_version(pkg_management_decoded_content, dependency_name)
                            logger.debug('{} is using {} version {}'.format(d, dependency_name, found_version))
                            has_test = has_pytest(d, pkg_management_decoded_content)
                            ver_match = target_version == found_version
                            write_if_not_exist('{}-{}'.format(dependency_name, found_version),
                                               '{} | {} | {}'.format(d, res_obj.name, appr))

                        if (has_req or has_setup) and has_test and ver_match and appr > 2:
                            logger.debug('Found usable dependent {}'.format(d))
                            prop_dependents.append(d)
                            write_if_not_exist('usable', dependency_name + '||' + d)
                elif code_search_resp.status_code == 403:
                    write_if_not_exist('Failed-{}'.format(dependency_name), d)

    print(prop_dependents)
    assert len(prop_dependents) == 20

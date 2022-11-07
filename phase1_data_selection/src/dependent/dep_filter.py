import re
import base64
import time
import random
import requests
from loguru import logger

from src.util.token_limit import token_limit
from src.util.constants import TOKENS
from src.util.util import get_ver_major, mapping_resp_to_generic


def has_content(str_owner_repo, str_content):
    """
    Checking if repo contains content/file
    :param str_owner_repo: repo full name, e.g. owner/repo
    :param str_content: file name
    :return: requests response
    """
    base_url = 'https://api.github.com/repos/{}/contents/{}'
    url = base_url.format(str_owner_repo, str_content)
    token = token_limit(TOKENS)
    if token is not None:
        GITHUB_HEADERS = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'token ' + base64.b64decode(token).decode()
        }
        time.sleep(random.uniform(0, 1))
        resp = requests.get(url, headers=GITHUB_HEADERS)
    else:
        raise ValueError('Running out github access limit')
    return resp


def extract_dependency_version(src_content, dependency_name):
    """
    Extract used dependency version from source content.
    :param src_content: e.g. requirements.txt or setup.py
    :param dependency_name: target dependency name
    :return: version number or None
    """
    regex = '{}==(\\d+\\.(?:\\d+\\.)*\\d+)'
    version_regex = re.compile(regex.format(dependency_name))
    se = version_regex.search(src_content)
    version = None if se is None else se.group().split('==')[1]
    return version


def has_pytest(str_owner_repo, req_setup):
    """
    Checking if repo uses pytest
    :param str_owner_repo: repo full name, e.g. owner/repo
    :param req_setup: e.g. requirements.txt or setup.py
    :return: boolean
    """
    repo_name = str_owner_repo.split('/')[1]
    if repo_name != 'pytest':
        return 'pytest' in req_setup
    else:
        return True


def find_target_version(dependency_generic_object):
    """
    Find a proper version as primary option
    :param dependency_generic_object: Generic object from Libraries.io Search api response
    :return: version string
    """
    ls_versions = dependency_generic_object.versions
    latest_major_version = get_ver_major(ls_versions[len(ls_versions) - 1].number)
    target_version = ''
    for i in reversed(dependency_generic_object.versions):
        if latest_major_version - get_ver_major(i.number) == 1:
            target_version = i.number
            break
    logger.debug('Found the latest of the second last major version number {}'.format(target_version))
    return target_version


def pkg_management_validation(str_owner_repo):
    resp = has_content(str_owner_repo, 'requirements.txt')
    if resp.status_code == 200:
        return resp
    else:
        resp = has_content(str_owner_repo, 'setup.py')
        return resp


# res = has_content('FranckLejzerowicz/metagenomix', 'setup.py')
# res_obj = mapping_resp_to_generic(res)
# decoded = base64.b64decode(res_obj.content).decode()
# print(extract_dependency_version(decoded, 'pandas'))

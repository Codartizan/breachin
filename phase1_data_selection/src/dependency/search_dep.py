import json

import requests
from loguru import logger

from src.util.constants import LIBRARIES_IO_API_KEY, LIBRARIES_IO_BASE_URL
from src.util.generic import Generic
from src.util.util import get_ver_major

query_params = {
    "languages": "python",
    "api_key": LIBRARIES_IO_API_KEY,
    "sort": "rank",  # sorted by source rank
    "platforms": "pypi"  # search in pypi platform
}

logger.debug('Searching highest source rank dependencies from Libraries.io')
response = requests.get(f"{LIBRARIES_IO_BASE_URL}/search", params=query_params).json()
logger.debug('Search result contains {} items from Libraries.io'.format(len(response)))


def search_dependency_by_rank():
    """
    Search dependency by source rank on Libraries.io
    :return: List of top 30 candidate dependency, generic object type
    """
    candidate_projects = []  # filtered projects

    for i in response:
        proj = json.loads(json.dumps(i), object_hook=Generic.from_dict)  # convert json to object
        if proj.repository_url is not None and proj.repository_url.startswith('https://github.com'):
            if get_ver_major(proj.versions[len(proj.versions) - 1].number) - get_ver_major(
                    proj.versions[0].number) >= 1:
                candidate_projects.append(proj)

    logger.debug('Found {} projects satisfied all conditions'.format(len(candidate_projects)))

    return candidate_projects


def find_research_version(dependency):
    """
    Extract the newest of the second last version
    :param dependency: Generic object of top rank dependency search from Libraries.io
    :return:
    """
    index = ''
    latest_major_version = str(get_ver_major(dependency.versions[len(dependency.versions) - 1].number) - 1)
    for i in dependency.versions:
        if i.number.startswith(latest_major_version):
            index = dependency.versions.index(i)
    logger.debug('Found proper version {}'.format(dependency.versions[index].number))
    return dependency.versions[index].number, dependency.versions[index].published_at


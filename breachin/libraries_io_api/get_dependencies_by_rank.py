import json

import requests
import semver
from loguru import logger

from breachin.libraries_io_api.constants import LIBRARIES_IO_API_KEY, LIBRARIES_IO_BASE_URL
from breachin.generic import Generic

query_params = {
    "languages": "python",
    "api_key": LIBRARIES_IO_API_KEY,
    "sort": "rank",  # sorted by source rank
    "platforms": "pypi",  # search in pypi platform
    "page": 1
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


def get_ver_major(ver):
    """
    This is function return an int type of major version of a semantic version
    :param ver: String, input must contain at least one semantic versioning delimiter
    :return: major version string
    """
    try:
        major = semver.VersionInfo.parse(ver).major
    except ValueError:
        major = ver.split('.')[0]
    return int(major)



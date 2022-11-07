# This file provides general utilities
import semver
import json
from src.util.generic import Generic


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


def repo_full_name(github_url):
    """
    Build repository full name, owner/repo_name
    :param github_url: Repository GitHub url
    :return: String owner/repo_name
    """
    base_url = 'https://github.com/'
    return github_url.removeprefix(base_url)


def write_if_not_exist(filename, content):
    """
    Checking if content exists in the file, if not, write it in
    :param filename: filename
    :param content: string
    :return: if it is exists
    """
    with open('/Users/tshi/PycharmProjects/softeng795/docs/{}.txt'.format(filename), 'a+') as file:
        file.seek(0)  # set position to start of file
        lines = file.read().splitlines()  # now we won't have those newlines
        if content in lines:
            return False
        else:
            file.write(content + "\n")
            return True


def mapping_resp_to_generic(resp):
    """
    Mapping api response json payload to Generic type object
    :param resp: requests response type
    :return: Generic type object
    """
    resp_obj = json.loads(json.dumps(resp.json()), object_hook=Generic.from_dict)
    return resp_obj

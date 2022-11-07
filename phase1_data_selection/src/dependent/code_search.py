import base64
import json
import time
import random

import requests
from loguru import logger

from src.util.constants import TOKENS
from src.util.generic import Generic
from src.util.token_limit import token_limit

base_url = 'https://api.github.com/search/code?q={}+in:file+repo:{}'


def dep_appearance(keyword, str_owner_repo):
    """
    Get dependency keyword appears in repo
    :param keyword: term
    :param str_owner_repo: owner/repo
    :return: requests response
    """
    url = base_url.format(keyword, str_owner_repo)
    token = token_limit(TOKENS)
    resp = None
    if token is not None:
        GITHUB_HEADERS = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'token ' + base64.b64decode(token).decode()
        }
        time.sleep(random.uniform(0, 1))
        resp = requests.get(url, headers=GITHUB_HEADERS)
        if resp.status_code == 200:
            return resp
        elif resp.status_code == 403:
            logger.error('{}-{}'.format(token, resp.text))
    return resp


def count_appearance(resp, keyword, str_owner_repo):
    """
    Count appearance of keyword in *.py files
    :param resp: requests response
    :param keyword: term
    :param str_owner_repo: owner/repo
    :return:
    """
    count = 0
    items = json.loads(resp.text)['items']
    logger.debug('{} appears in {} {} times in all file type'.format(keyword, str_owner_repo, len(items)))
    for i in items:
        item = json.loads(json.dumps(i), object_hook=Generic.from_dict)
        if item.name != 'setup.py' and item.name.endswith('.py'):
            count += 1
    return count


def file_dep_appearance(resp, filename):
    """
    Check if file appears with keyword
    :param resp: requests response
    :param filename: filename
    :return: boolean
    """
    files = []
    items = json.loads(resp.text)['items']
    for i in items:
        item = json.loads(json.dumps(i), object_hook=Generic.from_dict)
        files.append(item.name)
    return filename in files




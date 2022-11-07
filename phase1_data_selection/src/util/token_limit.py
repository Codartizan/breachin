import base64
import json
import secrets

import requests

from src.util.generic import Generic
from loguru import logger


def token_limit(tokens):
    """
    GitHub PAT has rate limit. This method is to find out a workable PAT from a given list
    :param tokens: a list of base64 encoded token string
    :return: PAT string
    """
    token = None
    remaining = 0
    while remaining < 1:
        token = secrets.choice(tokens)
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': 'token ' + base64.b64decode(token).decode()
        }
        resp = requests.get('https://api.github.com/rate_limit', headers=headers)

        if resp.status_code == 200:
            body = json.loads(json.dumps(resp.json()), object_hook=Generic.from_dict)
            remaining = body.rate.remaining

    logger.info('{}-{} rate limit remaining'.format(token, remaining))
    return token

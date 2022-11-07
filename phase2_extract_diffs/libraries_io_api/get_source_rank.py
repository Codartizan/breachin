import json

import requests

from phase2_extract_diffs.generic import Generic
from phase2_extract_diffs.libraries_io_api.constants import LIBRARIES_IO_API_KEY, LIBRARIES_IO_BASE_URL

query_params = {
    "api_key": LIBRARIES_IO_API_KEY,
}


def get_dep_source_rank(dep_name):
    response = requests.get(f"{LIBRARIES_IO_BASE_URL}" + "/pypi/{}/sourcerank".format(dep_name),
                            params=query_params).json()
    proj = json.loads(json.dumps(response), object_hook=Generic.from_dict)

    return proj

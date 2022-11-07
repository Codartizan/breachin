import json

import requests

from src.util.constants import LIBRARIES_IO_API_KEY, LIBRARIES_IO_BASE_URL
from src.util.generic import Generic

query_params = {
    "api_key": LIBRARIES_IO_API_KEY,
}

response = requests.get(f"{LIBRARIES_IO_BASE_URL}/pypi/Django/dependents", params=query_params).json()

dependents = []

for i in response:
    proj = json.loads(json.dumps(i), object_hook=Generic.from_dict)  # convert json to object
    dependents.append(proj)

for p in dependents:
    print(p.package_manager_url)
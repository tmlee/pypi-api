import requests, json

PYPI_URL = "https://pypi.python.org/pypi"

def fetch(package_name):
    url = '{pypi_url}/{package_name}/json'.format(pypi_url=PYPI_URL, package_name=package_name)
    r = requests.get(url)

    if r.status_code == requests.codes.ok:
        return json.dumps(r.json())
    else:
        r.raise_for_status()

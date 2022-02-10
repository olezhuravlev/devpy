import os
from pprint import pprint

import requests

TOKEN = "???"
HEADERS = {"Authorization": "OAuth " + TOKEN}


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        destination_path = "/" + file_path
        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": destination_path, "overwrite": "true"},
            headers=HEADERS)

        response.raise_for_status()

        data = response.json()
        pprint(data)

        href = data["href"]

        with open(file_path, "rb") as f:
            response = requests.put(href, files={"file": f})

        response.raise_for_status()

        return response.status_code


if __name__ == '__main__':
    uploader = YaUploader(TOKEN)
    result = uploader.upload(os.path.basename(__file__))
    print(result)

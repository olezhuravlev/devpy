import datetime
from pprint import pprint

import requests


class StackOverflowLoader:
    def __init__(self):
        pass

    def get_questions(self):

        req_params = {
            "fromdate": "1644278400",
            "order": "desc",
            "page": 0,
            "pagesize": 100,
            "sort": "creation",
            "tagged": "python",
            "site": "stackoverflow"
        }

        result = []
        while True:

            req_params["page"] += 1
            response = requests.get(
                "https://api.stackexchange.com/2.3/questions",
                params=req_params)

            response.raise_for_status()

            data = response.json()

            for question in data["items"]:
                creation_date = datetime.datetime.fromtimestamp(question["creation_date"])
                title = question["title"]
                result.append(f"{creation_date}: {title}")

            print("Page", req_params["page"])

            if not data["has_more"]:
                break

        print("Questions obtained:", len(result), "on", req_params["page"], "pages")
        return result


if __name__ == '__main__':
    uploader = StackOverflowLoader()
    result = uploader.get_questions()
    pprint(result)

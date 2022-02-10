import os
import requests
from pprint import pprint

GIFS_DIR = "gifs"


def test():
    response = requests.get("https://www.reddit.com/r/gifs.json?limit=25", headers={"user-agent": "some"})

    response.raise_for_status()

    posts = response.json()["data"]["children"]
    for post in posts:
        url = post["data"]["url"]
        if "imgur.com" not in url:
            continue
        url = url.replace(".gifv", ".gif")

        gif_response = requests.get(url)
        gif_response.raise_for_status()

        title: str = post["data"]["title"]
        title = "".join(x for x in title if x.isalnum() or x.isspace())
        # OK! destination_path = "W:/JetBrains/PycharmProjects/devpy/9.http.requests/gifs/" + title + ".gif"
        # OK! destination_path = os.path.join(os.path.dirname(__file__), GIFS_DIR, title + ".gif")
        destination_path = os.path.join(GIFS_DIR, title + ".gif")
        with open(destination_path, "wb") as f:
            f.write(gif_response.content)
            print(title)

    # pprint(posts)


if __name__ == '__main__':
    test()

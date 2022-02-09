import json


class JsonParser:
    def __init__(self, filename):
        with open(filename, encoding="UTF-8") as f:
            self.data = json.load(f)

    def print(self):

        unique_words = {}

        for item in self.data["rss"]["channel"]["items"]:
            words = item["description"].split()
            for word in words:
                if len(word) > 6:
                    unique_words[word] = len(word)

        unique_words_list = [(k, v) for k, v in unique_words.items()]
        sorted_list = sorted(unique_words_list, key=lambda item: item[1], reverse=True)
        return sorted_list[:10]


if __name__ == '__main__':
    parser = JsonParser("newsafr.json")
    print(parser.print())

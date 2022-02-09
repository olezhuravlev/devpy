import xml.etree.ElementTree


class XmlParser:
    def __init__(self, filename):
        with open(filename, encoding="UTF-8") as f:
            self.data = xml.etree.ElementTree.parse(f).getroot()

    def print(self):

        unique_words = {}

        # for channel in self.data:
        #     for node in channel:
        #
        #         if node.tag != "item" or "id" not in node.attrib:
        #             continue
        #
        #         for description in node:
        #             if description.tag != "description":
        #                 continue
        #
        #             words = description.text.split()
        #             for word in words:
        #                 if len(word) > 6:
        #                     unique_words[word] = len(word)

        for description in self.data.findall("channel/item/description"):
            words = description.text.split()
            for word in words:
                if len(word) > 6:
                    unique_words[word] = len(word)

        unique_words_list = [(k, v) for k, v in unique_words.items()]
        sorted_list = sorted(unique_words_list, key=lambda item: item[1], reverse=True)
        return sorted_list[:10]


if __name__ == '__main__':
    parser = XmlParser("newsafr.xml")
    print(parser.print())

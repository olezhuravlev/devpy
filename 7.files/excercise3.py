class FileCollector:

    def __init__(self, *filenames):
        self.files_length = []
        for filename in filenames:
            num_lines = self.get_file_length(filename)
            self.files_length.append((filename, num_lines))

    def get_file_length(self, filename):
        num_rows = sum(1 for line in open(filename, encoding="UTF-8"))
        return num_rows

    def write_to_file(self, filename):
        sorted_list = sorted(self.files_length, key=lambda item: item[1])
        with open(filename, "w+", encoding="UTF-8") as destination:
            for source_filename in sorted_list:
                with open(source_filename[0], encoding="UTF-8") as source:
                    for row in source:
                        destination.write(row)


if __name__ == '__main__':
    file_collector = FileCollector("1.txt", "2.txt", "3.txt")
    file_collector.write_to_file("4.txt")

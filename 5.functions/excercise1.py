import data, Utils


def get_document_by_num(doc_num):
    """
    Function returns document found by its number.
    """
    for document in data.documents:
        if document["number"] == doc_num:
            return document

    return None


def get_shelf_by_document_num(doc_num):
    """
    Function returns shelf number found by document number.
    """
    for shelf_num, shelf_docs in data.directories.items():
        if doc_num in shelf_docs:
            return shelf_num

    return None


def print_all_docs():
    for document in data.documents:
        print(document["type"], document["number"], document["name"])


def call_function(func):
    if func == "p":
        doc_num = Utils.get_parameter("Enter document number:", result_type=str)
        doc = get_document_by_num(doc_num)
        if doc is None:
            print("No document found")
        else:
            print(doc["name"])

    elif func == "s":
        doc_num = Utils.get_parameter("Enter document number:", result_type=str)
        shelf = get_shelf_by_document_num(doc_num)
        if shelf is None:
            print("No document found")
        else:
            print(shelf)
    elif func == "l":
        print_all_docs()
    elif func == "a":
        doc_num = Utils.get_parameter("Enter document number:", result_type=str)
        doc_type = Utils.get_parameter("Enter document type:", result_type=str)
        doc_name = Utils.get_parameter("Enter document owner's name:", result_type=str)
        shelf_num = Utils.get_parameter("Enter shelf number for the document:", result_type=int, interval_begin=1,
                                        interval_end=3)
        data.documents.append({"type": doc_type, "number": doc_num, "name": doc_name})
        data.directories[str(shelf_num)].append(doc_num)
        print(data.documents)
        print(data.directories)


if __name__ == '__main__':
    #"p", "s", "l", "a".
    call_function("a")

import data, Utils


def delete_document_from_shelf(doc_num):
    shelf_num_found = None
    for shelf_num, shelf_docs in data.directories.items():
        if doc_num in shelf_docs:
            shelf_num_found = shelf_num
            break

    if shelf_num_found == None:
        print("No shelf found")
    else:
        data.directories[shelf_num_found].remove(doc_num)


def add_document_num_to_shelf(shelf_num, doc):
    data.directories[str(shelf_num)].append(doc["number"])


def add_shelf(shelf_num):
    if str(shelf_num) in data.directories:
        print("Shelf already exists!")
        return
    data.directories[str(shelf_num)] = []


def delete_document_by_num(doc_num):
    doc_idx_found = None
    for idx, document in enumerate(data.documents):
        if document["number"] == doc_num:
            doc_idx_found = idx
            break

    if doc_idx_found == None:
        print("No document found")
    else:
        data.documents.pop(doc_idx_found)

    delete_document_from_shelf(doc_num)


def get_document_by_num(doc_num):
    """
    Function returns document found by its number.
    """
    for document in data.documents:
        if document["number"] == doc_num:
            return document

    return None


def move_document(doc_num, shelf_num):
    doc = get_document_by_num(doc_num)
    if (doc == None):
        print("No document found")
        return
    delete_document_from_shelf(doc_num)
    add_document_num_to_shelf(shelf_num, doc)


def call_function(func):
    if func == "d":
        doc_num = Utils.get_parameter("Enter document number:", result_type=str)
        delete_document_by_num(doc_num)

    elif func == "m":
        doc_num = Utils.get_parameter("Enter document number:", result_type=str)
        shelf_num = Utils.get_parameter("Enter shelf number:", result_type=int, interval_begin=1, interval_end=3)
        move_document(doc_num, shelf_num)

    elif func == "as":
        new_shelf_num = Utils.get_parameter("Enter new shelf number:", result_type=int)
        add_shelf(new_shelf_num)
        print(data.directories)


if __name__ == '__main__':
    # "d", "m", "as".
    call_function("as")

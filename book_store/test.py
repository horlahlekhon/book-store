def valid_book(book):
    if('name' in book and 'price' in book and 'isbn' in book):
        return True
    else:
        return False


def valid_put_book(book):
    if('name' in book and 'price' in book):
        return True
    else:
        return False


valid_object = {
    'name': "Das zein",
    'price': 10.99,
    'isbn': 1299292929929292
}

missing_name = {
    'price': 10.99,
    'isbn': 1299292929929292
}

missing_price = {
    'name': "Das zein",
    'isbn': 1299292929929292
}

missing_isbn = {
    'name': "Das zein",
    'price': 10.99,
}

empty_dict = {}

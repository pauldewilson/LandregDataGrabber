def return_list_urls_from_txtfile():
    """
    :return: list of all the URLs from the url_txtfile in root
    """
    with open(r'urls_txtfile.txt', 'r') as txtfile:
        return [r.replace('\n', '') for r in txtfile.readlines() if '#' not in r]
